from flask_pymongo import PyMongo
from bson.objectid import ObjectId

class UsersDb:
    
    def __init__(Self, users):
        Self.users = users

    def get_user_by_name(self, name: str) -> User:
        user = self.users.find_one({"name": name})
        if user is None:
            return None
        return User(user["name"], user["_id"], user["passwd"])
    
    def get_user_by_id(self, user_id: str) -> User:
        user = self.users.find_one({"_id": ObjectId(user_id)})
        if user is None:
            return None
        return User(user["name"], user["_id"], user["passwd"])
    
    def add_user(self, name: str, passwd: str) -> None:
        self.users.insert_one({"name": name, "passwd": passwd})

    def clear_all(self):
        self.users.delete_many({})


class ChoresDb:
    def __init__(self, chores):
        self.chores = chores
    
    def get_all_chores(self):
        return [Chore.create(chore) for chore in self.chores.find()]
    
    def add_chore(self, chore: Chore):
        self.chores.insert_one(chore.json)

    def clear_all(self):
        self.chores.delete_many({})


class DbManager:
    mongo: PyMongo = None
    users: UsersDb = None
    chores: ChoresDb = None
    
    @staticmethod
    def init(app):
        app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
        mongo = PyMongo(app)
        DbManager.users = UsersDb(mongo.db.users)
        DbManager.chores = ChoresDb(mongo.db.chores)