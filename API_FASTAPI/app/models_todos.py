from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import declarative_base

BaseTodos = declarative_base()

class Todo(BaseTodos):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    completed = Column(Boolean)