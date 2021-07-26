from dataclasses import dataclass
from datetime import datetime

@dataclass
class TodoModel:
    todo_id: int
    title: str
    body: str
    is_completed: bool
    created_at: datetime
    # due: datetime
    priority: int

    def to_dict(self):
        return {"todo_id":self.todo_id,
            "title":self.title,
            "body":self.body,
            "is_completed":self.is_completed,
            "created_at":self.created_at,
            "priority" : self.priority
            }