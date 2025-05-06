import asyncpg
from config import settings

class PostgresDB:
    def __init__(self):
        self.pool = None

    async def connect(self):
        if not self.pool:
            self.pool = await asyncpg.create_pool(
                user=settings.DB_USER,
                password=settings.DB_PASS,
                database=settings.DB_NAME,
                host=settings.DB_HOST,
                port=settings.DB_PORT
            )

    async def fetch_vehicle_status(self, name):
        await self.connect()
        async with self.pool.acquire() as conn:
            result = await conn.fetchrow("SELECT status FROM vehicles WHERE name = $1", name)
            return result["status"] if result else None

    async def insert_log(self, car, action, member, notes):
        await self.connect()
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO work_logs (car, action, member, notes) VALUES ($1, $2, $3, $4)",
                car, action, member, notes
            )