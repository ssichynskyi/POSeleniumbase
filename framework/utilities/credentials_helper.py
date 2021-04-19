import os


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


normal_user = User(
    login=os.getenv('STANDARD_USER_LOGIN'),
    password=os.getenv('STANDARD_USER_PASSWORD')
)
locked_out_user = User(
    login=os.getenv('LOCKED_OUT_USER_LOGIN'),
    password=os.getenv('LOCKED_OUT_USER_PASSWORD')
)
