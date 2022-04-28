from sqlalchemy import Column, Integer, Text
from models.base import Base


class Title(Base):
    __tablename__ = "titles"
    id = Column(Text, primary_key=True)
    type = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    release_year = Column(Integer, nullable=False)
    rating = Column(Text, nullable=False)
    duration = Column(Text, nullable=False)
    genre = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
