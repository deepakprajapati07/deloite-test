# app/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator

MYSQL_DB_HOSTNAME = "localhost"
MYSQL_DB_PORT = 3306
MYSQL_DB_NAME = "demo"
MYSQL_DB_USERNAME = "root"
MYSQL_DB_PASSWORD = "admin"

# MySQL connection string
MYSQL_DATABASE_URL = (
    f"mysql+aiomysql://{MYSQL_DB_USERNAME}:{MYSQL_DB_PASSWORD}"
    f"@{MYSQL_DB_HOSTNAME}:{MYSQL_DB_PORT}/{MYSQL_DB_NAME}"
)

# Async Engine
engine = create_async_engine(
    MYSQL_DATABASE_URL,
    echo=False,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
)


# Session and Base
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Correct return type
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session