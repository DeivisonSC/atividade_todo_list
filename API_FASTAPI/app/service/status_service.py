from sqlalchemy import func

def calculate_stats(db_todos, db_logs, TodoModel, LogModel):
    total_todos = db_todos.query(TodoModel).count()
    completed = db_todos.query(TodoModel)\
        .filter(TodoModel.completed == True)\
        .count()

    pending = total_todos - completed

    total_logs = db_logs.query(LogModel).count()

    most_action = db_logs.query(
        LogModel.action,
        func.count(LogModel.action).label("count")
    ).group_by(LogModel.action)\
     .order_by(func.count(LogModel.action).desc())\
     .first()

    most_frequent = most_action[0] if most_action else None

    avg_logs = 0
    if total_todos > 0:
        avg_logs = total_logs / total_todos

    return {
        "totalTodos": total_todos,
        "completed": completed,
        "pending": pending,
        "totalLogs": total_logs,
        "mostFrequentAction": most_frequent,
        "averageLogsPerTodo": round(avg_logs, 2)
    }