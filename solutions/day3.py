from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def __init__(self, data, expectedValue1=-1, expectedValue2=-1):
        super().__init__(data, expectedValue1, expectedValue2)
        self.used = set()

    def isSymbol(self, c):
        return not c.isdigit() and c != "."

    def getFullNumber(self, row, x):
        self.used.add((row, x))
        startIndex = x
        endIndex = x

        while startIndex > 0 and self.data[row][startIndex - 1].isdigit():
            startIndex -= 1

        while endIndex < len(self.data[row]) and self.data[row][endIndex].isdigit():
            endIndex += 1

        for i in range(startIndex, endIndex):
            self.used.add((row, i))

        return int(self.data[row][startIndex:endIndex])

    def getGearRatio(self, y, x):
        # Look for numbers adjacent
        nums = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    (i == 0 and j == 0)
                    or y + i < 0
                    or y + i >= len(self.data)
                    or x + j < 0
                    or x + j >= len(self.data[y + i])
                ):
                    continue
                if self.data[y + i][x + j].isdigit():
                    if (y + i, x + j) not in self.used:
                        nums.append(self.getFullNumber(y + i, x + j))

        if len(nums) == 2:
            return nums[0] * nums[1]

        return 0

    def part2(self):
        s = 0
        for j in range(len(self.data)):
            for i in range(len(self.data[j])):
                if self.isSymbol(self.data[j][i]):
                    s += self.getGearRatio(j, i)

        return s
