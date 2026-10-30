from ai_deep_research_orchestrator.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url=settings.DATABASE_URL
)


session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)



class Base(DeclarativeBase):
    pass


async def get_db():
    async with session_factory() as db:
        yield db