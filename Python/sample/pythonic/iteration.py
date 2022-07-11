#!/usr/bin/python3


class IterableList:
    def __init__(self):
        self._data = [1, 2, 3, 4]
        self._index = 0

    def __iter__(self):
        return self
        # return iter(self._data)

    def __next__(self):
        try:
            answer = self._data[self._index]
        except IndexError:
            self._index = 0
            raise StopIteration from IndexError
        else:
            self._index += 1
            return answer


class Sequence:
    def __init__(self):
        self._data = [1, 2, 3, 4]

    def __getitem__(self, index):
        return self._data[index]
        # return iter(self._data)


def main():
    iterableList = IterableList()
    for i in iterableList:
        print(i)

    sequence = Sequence()
    for i in sequence:
        print(i)
    pass


if __name__ == "__main__":
    main()
