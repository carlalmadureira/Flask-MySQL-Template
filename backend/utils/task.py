from typing import Dict
import uuid

class Task:
    def __init__(self, title:str, category:str, status:str, color:str):
        self.title = title
        self.category = category
        self.status = status
        self.color = color

    def set_task(self) -> Dict:

        task = {
            id: str(uuid.uuid4()),
            "title": self.title,
            "category": self.category,
            "status": self.status,
            "color": self.color
        }

        return task