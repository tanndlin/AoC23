import abc
import time


class SolutionBase:
    def __init__(self, data, expectedValue1=-1, expectedValue2=-1):
        # Remove redundant whitespace
        self.data = [" ".join(i.split()) for i in data]
        self.expectedValue1 = expectedValue1
        self.expectedValue2 = expectedValue2

    @abc.abstractmethod
    def part1(self) -> int:
        pass

    @abc.abstractmethod
    def part2(self) -> int:
        pass

    def test(self):
        if self.expectedValue1 == -1:
            print("No expected value provided")
            return

        failed = False
        res1 = self.part1()
        if self.expectedValue1 != res1:
            print(f"WARN part 1: Expected {self.expectedValue1}, got {res1}")
            failed = True

        res2 = self.part2()
        if self.expectedValue2 != -1 and self.expectedValue2 != res2:
            print(f"WARN part 2: Expected {self.expectedValue2}, got {res2}")
            failed = True

        if not failed:
            print("All tests passed")
        else:
            print("Some tests failed")
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
