# user class

class User:
    TODAY =
    def __init__(self, username, password, email, birthday):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f"Username: {self.username}\npassword: {self.password}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

    def __eq__(self, other):
        return __

    def get_age(self):
        b_day = util.parser.parse(self.birthday)
        today = dt.datetime.now()
        return (today - b_day).days




if __name__ == "__main__":
    user = User(username="Fred", password="password", email="fred@some.com", birthday="2/7/24")
    print(user.username)
    print(user)
