import math

from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def preprocess(self):
        self.nodes = {}
        self.instructions = self.data[0]

        for line in self.data[1:]:
            root = line.split(" = ")[0]
            pair = line.split(" = ")[1]
            a = pair.split(", ")[0].replace("(", "")
            b = pair.split(", ")[1].replace(")", "")

            self.nodes[root] = (a, b)

    def part1(self):
        cur = "AAA"
        i = 0
        steps = 0
        while cur != "ZZZ":
            instruction = self.instructions[i]
            i = (i + 1) % len(self.instructions)
            cur = self.nodes[cur][0 if instruction == "L" else 1]
            steps += 1

        return steps

    def part2(self):
        curNodes = [node for node in self.nodes if node.endswith("A")]
        totalSteps = [0] * len(curNodes)

        for j, node in enumerate(curNodes):
            cur = node
            i = 0
            steps = 0

            while not cur.endswith("Z"):
                instruction = self.instructions[i]
                i = (i + 1) % len(self.instructions)
                cur = self.nodes[cur][0 if instruction == "L" else 1]
                steps += 1

            totalSteps[j] = steps

        return math.lcm(*totalSteps)
