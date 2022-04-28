from tkinter.tix import Tree
from sqlalchemy import Column, Integer, Text, ForeignKey
from models.base import Base


class Staff(Base):
    __tablename__ = "staffs"
    id = Column(Text, primary_key=True)
    director = Column(Text)
    cast = Column(Text)
    show_id = Column(Integer, ForeignKey("titles.id"), nullable=False)
