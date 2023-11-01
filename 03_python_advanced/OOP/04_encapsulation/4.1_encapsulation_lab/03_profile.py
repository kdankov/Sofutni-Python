class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        if not 5 <= len(username) <= 15:
            raise ValueError('The username must be between 5 and 15 characters.')

        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not (len(password) >= 8 and any(x.isupper() for x in password) and any(x.isdigit() for x in password)):
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'




correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
