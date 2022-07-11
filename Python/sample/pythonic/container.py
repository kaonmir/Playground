#!/usr/bin/python3


class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contains__(self, coord):
        return coord in self.limits


def main():
    grid = Grid(4, 10)
    if (1, 2) in grid:
        print("success!")


if __name__ == "__main__":
    main()
