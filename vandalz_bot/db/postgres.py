import asyncpg
from config import DB_CONFIG

class PostgresDB:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(**DB_CONFIG)

    async def fetch_vehicle_status(self, name: str):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow("SELECT status FROM vehicles WHERE name=$1", name)
            return row["status"] if row else None

    async def insert_log(self, car, action, member, notes):
        async with self.pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO work_logs (car, action, member, notes)
                VALUES ($1, $2, $3, $4)
            """, car, action, member, notes)