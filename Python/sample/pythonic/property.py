#!/usr/bin/python3


class User:
    def __init__(self, username):
        self.username = username
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age: %d" % age)
        self._age = age


def main():
    user = User("kaonmir")
    user.age = -3
    user.age = 9
    print(user.age)


if __name__ == "__main__":
    main()
