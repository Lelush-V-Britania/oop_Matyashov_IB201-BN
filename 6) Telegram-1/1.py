class User:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    def check_password(self, password: str) -> bool:
        return self._password == password

    def set_password(self, old_password: str, new_password: str) -> bool:
        if self.check_password(old_password):
            self._password = new_password
            return True
        return False