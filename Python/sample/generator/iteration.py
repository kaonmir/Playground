#!/usr/bin/python3


class MappedRange:
    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped_range = range(start, end)

    def __getitem__(self, index):
        item = self._wrapped_range[index]
        return self._transformation(item)

    def __len__(self):
        return len(self._wrapped_range)


def main():
    a = [1, 2]
    print(a)
    mr = MappedRange(abs, -10, 5)
    print(list(mr))


if __name__ == "__main__":
    main()
