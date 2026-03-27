import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_TODOS = os.getenv("DATABASE_TODOS")
DATABASE_LOGS = os.getenv("DATABASE_LOGS")

engine_todos = create_engine(DATABASE_TODOS)
engine_logs = create_engine(DATABASE_LOGS)

SessionTodos = sessionmaker(bind=engine_todos)
SessionLogs = sessionmaker(bind=engine_logs)

def get_db_todos():
    db = SessionTodos()
    try:
        yield db
    finally:
        db.close()

def get_db_logs():
    db = SessionLogs()
    try:
        yield db
    finally:
        db.close()