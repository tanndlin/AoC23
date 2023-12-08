from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self):
        expected = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        s = 0
        for d in self.data:
            temp = d.split(": ")
            id = int(temp[0].split(" ")[1])

            subsets = temp[1].split("; ")

            flag = True
            for subset in subsets:
                bags = subset.split(", ")

                for bag in bags:
                    num = int(bag.split(" ")[0])
                    color = bag.split(" ")[1]

                    if num > expected[color]:
                        flag = False
                        break

            if flag:
                s += id

        return s

    def part2(self):
        s = 0
        for d in self.data:
            temp = d.split(": ")
            id = int(temp[0].split(" ")[1])

            subsets = temp[1].split("; ")
            mins = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for subset in subsets:
                bags = subset.split(", ")

                for bag in bags:
                    num = int(bag.split(" ")[0])
                    color = bag.split(" ")[1]

                    if mins[color] < num:
                        mins[color] = num

            s += mins["red"] * mins["green"] * mins["blue"]

        return s
