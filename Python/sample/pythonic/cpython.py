#!/usr/bin/python3


class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        prefix = "짝수" if index % 2 == 0 else "홀수"
        return f"[{prefix}] {value}"


def main():
    bl = BadList((0, 1, 2, 3, 4, 5))
    print(bl[0], bl[1])
    print("".join(bl))
    pass


if __name__ == "__main__":
    main()
