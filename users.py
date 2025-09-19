class User:
    users_db = {}
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.has_voted = False
    @classmethod
    def add_user(cls, username, password):
        if username in cls.users_db:
            return False
        cls.users_db[username] = User(username, password)
        return True
    @classmethod
    def authenticate(cls, username, password):
        user = cls.users_db.get(username)
        if user and user.password == password:
            return user
        return None
