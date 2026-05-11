// MCQ Exam App — Service Worker
// Bump CACHE_VERSION on every deploy that changes templates/JS/CSS so phones pick up fresh content.
const CACHE_VERSION = 'mcq-v5-2026-05-05';
const STATIC_CACHE = `${CACHE_VERSION}-static`;
const STATIC_ASSETS = [
  '/static/manifest.json',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png'
];

// On install: pre-cache only versioned static assets, skip waiting so the new SW activates immediately.
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(STATIC_CACHE).then(c => c.addAll(STATIC_ASSETS).catch(() => {}))
  );
  self.skipWaiting();
});

// On activate: delete every cache that isn't the current STATIC_CACHE — wipes old versions.
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== STATIC_CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Listen for "skipWaiting" message from the page (so updates apply on reload without uninstall).
self.addEventListener('message', e => {
  if (e.data && e.data.type === 'SKIP_WAITING') self.skipWaiting();
});

// Fetch strategy:
//   - Navigation requests (HTML pages) and API calls => NETWORK ONLY (never cache stale HTML/JSON).
//     If network fails, fall back to the cached "/" shell so installed PWAs don't hard-crash.
//   - Static assets (CSS/JS/images/icons) => network-first, cache for offline.
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const isApi  = url.pathname.startsWith('/api/');
  const isNav  = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');
  const isStaticAsset = url.pathname.startsWith('/static/') && !url.pathname.endsWith('manifest.json');

  // 1) HTML pages + API: always go to network. Don't pollute cache with templates/data.
  if (isNav || isApi) {
    e.respondWith(
      fetch(req).catch(() => {
        // Offline fallback for navigation only
        if (isNav) return caches.match('/') || caches.match('/static/manifest.json');
        return new Response(JSON.stringify({error: 'offline'}), {
          status: 503, headers: {'Content-Type': 'application/json'}
        });
      })
    );
    return;
  }

  // 2) Static assets: network-first, cache aside, fall back to cache when offline
  if (isStaticAsset || url.pathname === '/static/manifest.json') {
    e.respondWith(
      fetch(req).then(resp => {
        const clone = resp.clone();
        if (resp.ok) caches.open(STATIC_CACHE).then(c => c.put(req, clone));
        return resp;
      }).catch(() => caches.match(req))
    );
    return;
  }

  // 3) Anything else (cross-origin etc.): network-only, no caching
  e.respondWith(fetch(req).catch(() => caches.match(req)));
});
