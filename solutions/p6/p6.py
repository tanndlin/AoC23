import numpy as np

data = open("sample.txt").read().split("\n")

data[0] = " ".join(data[0].split())
data[1] = " ".join(data[1].split())

lengths = list(map(int, data[0].split(" ")[1:]))
distances = list(map(int, data[1].split(" ")[1:]))


def part1():
    ways = [0] * len(lengths)
    for race in range(len(lengths)):
        length = lengths[race]
        distance = distances[race]

        for speed in range(length):
            if (length - speed) * speed > distance:
                ways[race] += 1

    return np.prod(ways)


def part2():
    length = int("".join([str(i) for i in lengths]))
    distance = int("".join([str(i) for i in distances]))

    print(length, distance)

    ways = 0
    for speed in range(length):
        if (length - speed) * speed > distance:
            ways += 1

    return ways


print(part1())
print(part2())
