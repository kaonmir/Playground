#!/usr/bin/python3


class Iterable:
    def __init__(self):
        self._data = [1, 2, 3, 4]
        self._index = 0

    def __iter__(self):
        return self
        # return iter(self._data)

    def __next__(self):
        try:
            answer = self._data[self._index]
            self._index += 1
            return answer
        except IndexError:
            raise StopIteration from IndexError


def main():
    iterable = Iterable()
    for i in iterable:
        print(i)
    pass


if __name__ == "__main__":
    main()
