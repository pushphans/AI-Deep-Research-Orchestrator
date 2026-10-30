from sqlalchemy import UUID
import uuid
from ai_deep_research_orchestrator.core.db import Base
from sqlalchemy import Text, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped





class UserModel(Base):
    id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)




