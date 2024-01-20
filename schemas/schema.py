from pydantic import BaseModel
from typing import Optional

class PutTaskRequest(BaseModel):
    content: str
    user_id: Optional[str] = None
    task_id: Optional[str] = None
    is_done: bool = False