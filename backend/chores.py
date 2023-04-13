from .data_base_manager import DbManager
from .users import User

class Chore:
    def __init__(self, title: str, description: str, icon: str, duration: str, user_id: str) -> None:
        self.title = title
        self.description = description
        self.icon = icon
        self.duration = duration
        self.user_id = user_id

    @classmethod
    def create(cls, json: dict):
        return cls(json["title"], json["description"], json["icon"], json["duration"], json["user_id"])
    
    def add_to_db(self):
        

    @property
    def json(self):
        return {
            "title": self.title,
            "description": self.description,
            "icon": self.icon,
            "duration": self.duration,
            "user": self.user.name
        }
    
    @property
    def user(self) -> User:
        return DbManager.users.get_user_by_id(self.user_id)