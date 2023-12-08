from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def isSymbol(self, c):
        return not c.isdigit() and c != "."

    def isValidPartNumber(self, start, end, j):
        # Check for a symbol around this number
        startIndex = max(0, start - 1)
        endIndex = min(len(self.data[j]) - 1, end + 1)

        # Check above
        if j != 0:
            for k in range(startIndex, endIndex + 1):
                if self.isSymbol(self.data[j - 1][k]):
                    return True

        # Check below
        if j != len(self.data) - 1:
            for k in range(startIndex, endIndex + 1):
                if self.isSymbol(self.data[j + 1][k]):
                    return True

        # Check left
        if startIndex != 0:
            if self.isSymbol(self.data[j][startIndex]):
                return True

        # Check right
        if endIndex != len(self.data[j]) - 1:
            if self.isSymbol(self.data[j][endIndex]):
                return True

        return False

    def part1(self):
        s = 0
        i = 0
        j = 0
        while i != len(self.data) and j != len(self.data[i]):
            while i < len(self.data[j]):
                if self.data[j][i].isdigit():
                    start = i
                    end = i
                    while end < len(self.data[j]) and self.data[j][end].isdigit():
                        end += 1
                    end -= 1  # go back since we went one too far

                    # Do stuff
                    if self.isValidPartNumber(start, end, j):
                        s += int(self.data[j][start : end + 1])

                    i = end + 1
                else:
                    i += 1
            j += 1
            i = 0

        return s

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
        self.used = set()
        s = 0
        for j in range(len(self.data)):
            for i in range(len(self.data[j])):
                if self.isSymbol(self.data[j][i]):
                    s += self.getGearRatio(j, i)

        return s
