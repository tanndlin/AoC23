import math

from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def extrapolate(self, nums):
        # Take derivatives until the deriv is 0
        derivs = [nums]

        while not all([x == 0 for x in derivs[-1]]):
            newNums = []
            for i in range(len(derivs[-1]) - 1):
                newNums.append(derivs[-1][i + 1] - derivs[-1][i])
            derivs.append(newNums)

        for i in range(len(derivs) - 2, -1, -1):
            # Add last num of this row and last num of prev row, append here
            derivs[i].append(derivs[i][-1] + derivs[i + 1][-1])

        return derivs[0][-1]

    def part1(self):
        s = 0
        for line in self.data:
            s += self.extrapolate([int(x) for x in line.split(" ")])

        return s

    def interpolate(self, nums):
        # Take derivatives until the deriv is 0
        derivs = [nums]

        while not all([x == 0 for x in derivs[-1]]):
            newNums = []
            for i in range(len(derivs[-1]) - 1):
                newNums.append(derivs[-1][i + 1] - derivs[-1][i])
            derivs.append(newNums)

        for i in range(len(derivs) - 2, -1, -1):
            # Subtract first num of prev row, from first num of this row, prepend
            derivs[i].insert(0, derivs[i][0] - derivs[i + 1][0])

        return derivs[0][0]

    def part2(self) -> int:
        s = 0
        for line in self.data:
            s += self.interpolate([int(x) for x in line.split(" ")])

        return s
