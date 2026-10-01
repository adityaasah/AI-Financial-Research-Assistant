from __future__ import annotations

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, JSON, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    source = Column(String, nullable=True)
    doc_metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    chunks = relationship("Chunk", back_populates="document", cascade="all, delete-orphan")


Chunk = None  # type: ignore - forward reference placeholder for import ordering
