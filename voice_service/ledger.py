"""Daily spend ledger kept in the app database so restarts cannot reset the cap."""
import datetime as dt
from sqlalchemy import text


def init(engine):
    with engine.begin() as c:
        c.execute(text("""CREATE TABLE IF NOT EXISTS voice_usage (
            day VARCHAR(10) NOT NULL, device_id VARCHAR(64) NOT NULL, usd REAL NOT NULL DEFAULT 0,
            turns INTEGER NOT NULL DEFAULT 0, PRIMARY KEY (day, device_id))"""))


def today() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=5, minutes=30))).strftime("%Y-%m-%d")


def spent(engine, device_id) -> float:
    with engine.connect() as c:
        v = c.execute(text("SELECT usd FROM voice_usage WHERE day=:d AND device_id=:v"),
                      {"d": today(), "v": device_id}).scalar()
    return float(v or 0)


def add(engine, device_id, usd: float, turns: int = 0):
    p = {"d": today(), "v": device_id, "u": usd, "t": turns}
    with engine.begin() as c:
        n = c.execute(text("UPDATE voice_usage SET usd=usd+:u, turns=turns+:t WHERE day=:d AND device_id=:v"), p).rowcount
        if not n:
            c.execute(text("INSERT INTO voice_usage(day,device_id,usd,turns) VALUES(:d,:v,:u,:t)"), p)
