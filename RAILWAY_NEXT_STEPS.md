# Railway Second Service — Manual Steps

The sandbox couldn't authenticate to Railway. Complete these steps manually:

## 1. Push code first
```cmd
git push origin main --tags
```

## 2. Create second service on Railway
1. Go to https://railway.com/project/80d016ab-a223-4bf3-9a41-f7fde6ebc39b/
2. Click **"+ New Service"** → **"GitHub Repo"**
3. Select your repo, branch `main`
4. Name the service: `mcq-app-v2`
5. **Do NOT touch the existing `mcq-app` service**

## 3. Add Postgres
1. In the `mcq-app-v2` service → **"+ New"** → **"Database"** → **"Add PostgreSQL"**
2. Railway auto-sets `DATABASE_URL` in the service environment

## 4. Set environment variables
In `mcq-app-v2` service → Variables tab:
```
SECRET_KEY=<generate a strong random key>
ADMIN_PIN=<choose your PIN>
FLASK_DEBUG=0
```

## 5. Set start command
In `mcq-app-v2` service → Settings → Start Command:
```
gunicorn wsgi:app
```
Or use the existing `Procfile` (Railway reads it automatically).

## 6. Run migrations + seed on deploy
Add to Railway deploy command or run via Railway CLI after first deploy:
```bash
python -m alembic upgrade head
python scripts/seed_dev.py
python scripts/seed_exam_group2.py
python scripts/migrate_from_legacy.py
```

## 7. Verify
- `https://<new-service>.up.railway.app/healthz` should return `{"status":"ok","phase":"1"}`
- `https://<new-service>.up.railway.app/admin/login` — enter your PIN

## Note
The old service at `https://web-production-ac9f2.up.railway.app/` remains untouched until Phase 7 cutover.
