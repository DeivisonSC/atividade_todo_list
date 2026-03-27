from pydantic import BaseModel

class StatsResponse(BaseModel):
    totalTodos: int
    completed: int
    pending: int
    totalLogs: int
    mostFrequentAction: str | None
    averageLogsPerTodo: float