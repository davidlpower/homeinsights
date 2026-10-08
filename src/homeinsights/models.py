from datetime import datetime

from sqlalchemy import DateTime, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Reading(Base):
    __tablename__ = "readings"
    __table_args__ = (UniqueConstraint("entity_id", "recorded_at"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    entity_id: Mapped[str] = mapped_column(String(255), index=True)
    raw_state: Mapped[str] = mapped_column(String(255))
    value: Mapped[float | None]
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
