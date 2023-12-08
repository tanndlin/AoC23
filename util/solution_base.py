import abc
import time


class SolutionBase:
    def __init__(self, data, expectedValue=-1):
        # Remove redundant whitespace
        self.data = [" ".join(i.split()) for i in data]
        self.expectedValue = expectedValue

    @abc.abstractmethod
    def part1(self) -> int:
        pass

    @abc.abstractmethod
    def part2(self) -> int:
        pass

    def test(self):
        if self.expectedValue == -1:
            print("No expected value provided")
            return

        if self.expectedValue != self.part1():
            print(f"WARN: Expected {self.expectedValue}, got {self.part1()}")
            exit()

    def benchmark(self, epochs=10):
        def roundToMilli(n):
            return round(n * 1000) / 1000

        s = 0
        for i in range(epochs):
            start = time.time_ns()
            self.part1()
            end = time.time_ns()
            s += end - start

        print(f"Part 1: {roundToMilli(s / epochs/1_000_000)}ms")

        s = 0
        for i in range(epochs):
            start = time.time_ns()
            self.part2()
            end = time.time_ns()
            s += end - start

        print(f"Part 2: {roundToMilli(s / epochs/1_000_000)}ms")
