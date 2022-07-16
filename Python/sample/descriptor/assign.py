#!/usr/bin/python3


from turtle import hideturtle


class History1:
    def __init__(self, item):
        self.history = [item]

    def addItem(self, item):
        self.history.append(item)


class Traveller1:
    def __init__(self, city):
        self.current_city = city
        self.history = History1(city)

    def move(self, city):
        self.current_city = self
        self.history.addItem(city)

    def getHistory(self):
        return self.history.history


# ----------------------------------------------------------------


class History2:
    def __init__(self):
        self.current_item = None
        self.history = []

    def __get__(self, instance, owner):
        return self.current_item

    def __set__(self, insatnce, item):
        self.history.append(item)

    def getHistory(self):
        return self.history


class Traveller2:
    current_city = History2()

    def __init__(self, city):
        Traveller2.current_city = city

    def getHistory(self):
        return Traveller2.current_city


def main():
    traveller1 = Traveller1("Seoul1")
    traveller2 = Traveller2("Seoul2")

    print(f"Traveller1: {traveller1.current_city}")
    print(f"Traveller1: {traveller2.current_city}")

    print(
        f"Traveller1 current_city: {traveller1.current_city}, history: {traveller1.getHistory()}"
    )
    print(
        f"Traveller2 current_city: {traveller2.current_city}, history: {traveller2.getHistory()}"
    )


if __name__ == "__main__":
    main()
