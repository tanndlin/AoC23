import argparse
import importlib

from util.puzzle_reader import readPuzzle, readSample


def main():
    parser = argparse.ArgumentParser(description="Advent of Code solution runner")
    parser.add_argument("-d", "--day", type=int, help="Day to run")
    parser.add_argument(
        "-p", "--part", type=int, help="Optional: Specify a part to run"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="both",
        help="Specify whether to use the sample input, regular, or both",
    )
    parser.add_argument(
        "-b", "--benchmark", action="store_true", help="Optional: Benchmark"
    )
    parser.add_argument(
        "-t", "--test", action="store_true", help="Optional: Run tests for the day"
    )
    args = parser.parse_args()

    if args.day is None or args.day < 1 or args.day > 25:
        print("Please specify a valid day")
        return

    if args.input not in ["both", "input", "sample"]:
        print("Please specify a valid input type: [both, input, sample]")
        return

    sampleData = readSample(f"inputs/{args.day}/sample.txt")
    inputPuzzle = readPuzzle(f"inputs/{args.day}/input.txt")

    print(f"Day {args.day}")

    if args.input == "both" or args.input == "sample":
        sol = importlib.import_module(f"solutions.day{args.day}").Solution(*sampleData)
        print(f"Sample Part 1: {sol.part1()}")
        print(f"Sample Part 2: {sol.part2()}")

        if args.test:
            sol.test()
        print()

    if args.input == "both" or args.input == "input":
        sol = importlib.import_module(f"solutions.day{args.day}").Solution(inputPuzzle)
        print(f"Input Part 1: {sol.part1()}")
        print(f"Input Part 2: {sol.part2()}")
        print()

    if args.benchmark:
        sol = importlib.import_module(f"solutions.day{args.day}").Solution(inputPuzzle)
        sol.benchmark()


if __name__ == "__main__":
    main()
