from flask_login import mixins

class User (mixins.UserMixin):
    def __init__(self, name: str, user_id, passwd: str):
        self.name = name
        self.id = user_id
        self.passwd = passwd