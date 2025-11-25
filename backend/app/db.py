from databases import Database

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/blog"

database = Database(DATABASE_URL)

async def connect():
    await database.connect()

async def disconnect():
    await database.disconnect()