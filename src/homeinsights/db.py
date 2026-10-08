from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from homeinsights.settings import settings

engine = create_async_engine(settings.database_url)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
