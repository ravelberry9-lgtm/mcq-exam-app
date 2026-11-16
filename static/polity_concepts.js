/* Concept card page: one sub-card open at a time from nav, expand all, quick revise. */
(function(){
  var root=document.querySelector('.cg-topic');if(!root)return;
  var subs=[].slice.call(document.querySelectorAll('.cg-sub')),nav=[].slice.call(document.querySelectorAll('.cg-nav a'));
  function mark(id){nav.forEach(function(a){if(a.dataset.sub===id)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current');});
    var cur=document.querySelector('.cg-nav a[aria-current]');if(cur&&cur.scrollIntoView&&window.innerWidth<760)cur.scrollIntoView({block:'nearest',inline:'center'});}
  function show(id,scroll){var d=document.getElementById(id);if(!d)return;d.open=true;mark(id);
    if(scroll)d.scrollIntoView({block:'start',behavior:'smooth'});}
  nav.forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();show(a.dataset.sub,true);history.replaceState(null,'','#'+a.dataset.sub);});});
  subs.forEach(function(d){d.addEventListener('toggle',function(){if(d.open)mark(d.id);});});
  var start=(location.hash||'').slice(1)||root.dataset.open;
  if(start&&document.getElementById(start)){show(start,!!location.hash);if(new URLSearchParams(location.search).get('sub')){var h=document.getElementById(start);h.classList.add('hit');setTimeout(function(){h.classList.remove('hit')},2500);}}
  var ex=document.getElementById('cg-expand'),all=false;
  ex&&ex.addEventListener('click',function(){all=!all;subs.forEach(function(d){d.open=all;d.querySelectorAll('.cg-sec').forEach(function(s){s.open=all||s.hasAttribute('data-def');});});ex.textContent=all?'Collapse all':'Expand all';});
  document.querySelectorAll('.cg-sec[open]').forEach(function(s){s.setAttribute('data-def','')});
  var rv=document.getElementById('cg-revise');
  rv&&rv.addEventListener('click',function(){var on=root.classList.toggle('cg-revise');rv.setAttribute('aria-pressed',on?'true':'false');if(on)subs.forEach(function(d){d.open=true;d.querySelectorAll('.cg-sec.traps').forEach(function(s){s.open=true})});});
})();
