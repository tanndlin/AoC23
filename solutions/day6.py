import numpy as np

from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def preprocess(self):
        self.data[0] = " ".join(self.data[0].split())
        self.data[1] = " ".join(self.data[1].split())

        self.lengths = list(map(int, self.data[0].split(" ")[1:]))
        self.distances = list(map(int, self.data[1].split(" ")[1:]))

    def part1(self):
        ways = [0] * len(self.lengths)
        for race in range(len(self.lengths)):
            length = self.lengths[race]
            distance = self.distances[race]

            for speed in range(length):
                if (length - speed) * speed > distance:
                    ways[race] += 1

        return np.prod(ways)

    def part2(self):
        length = int("".join([str(i) for i in self.lengths]))
        distance = int("".join([str(i) for i in self.distances]))

        ways = 0
        for speed in range(length):
            if (length - speed) * speed > distance:
                ways += 1

        return ways
