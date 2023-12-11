import math

from util.solution_base import SolutionBase


class Solution(SolutionBase):
    # North, East, South, West
    _dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    _connects = {
        "|": [0, 2],  # North, South
        "-": [1, 3],  # East, West
        "L": [0, 1],  # North, East
        "J": [0, 3],  # North, West
        "7": [2, 3],  # South, West
        "F": [1, 2],  # East, South
    }

    # Converts a smybol at a pos to a list of potential neighbors
    def posToNeighbors(self, pos):
        sym = self.data[pos[1]][pos[0]]
        if sym == "S":
            return [(pos[0] + d[0], pos[1] + d[1]) for d in self._dirs]

        if sym not in self._connects:
            return []

        return [
            (pos[0] + self._dirs[d][0], pos[1] + self._dirs[d][1])
            for d in self._connects[sym]
        ]

    def preprocess(self):
        def tryAddNeighbors(a, b):
            if (
                a[0] < 0
                or a[0] >= len(self.data[0])
                or a[1] < 0
                or a[1] >= len(self.data)
            ):
                return

            if (
                b[0] < 0
                or b[0] >= len(self.data[0])
                or b[1] < 0
                or b[1] >= len(self.data)
            ):
                return

            if a not in self.posToNeighbors(b) or b not in self.posToNeighbors(a):
                return

            if a not in self.adj:
                self.adj[a] = [b]
            else:
                self.adj[a].append(b)

            if b not in self.adj:
                self.adj[b] = [a]
            else:
                self.adj[b].append(a)

            # Remove duplicates
            self.adj[a] = list(set(self.adj[a]))
            self.adj[b] = list(set(self.adj[b]))

        self.adj = {}

        for y, row in enumerate(self.data):
            for x, sym in enumerate(row):
                if sym == "S":
                    self.adj[(x, y)] = []
                    self.start = (x, y)

                potential = self.posToNeighbors((x, y))

                for p in potential:
                    tryAddNeighbors((x, y), p)

    def getCellsInLoop(self):
        queue = [self.start]
        visited = set()

        while len(queue) > 0:
            pos = queue.pop(0)

            if pos in visited:
                continue

            visited.add(pos)
            queue.extend(self.adj[pos])

        return visited

    def part1(self) -> int:
        return len(self.getCellsInLoop()) // 2

    def floodFill(self, pos, visited, inLoop):
        q = [pos]
        while len(q) > 0:
            pos = q.pop()

            if (
                pos[0] < 0
                or pos[0] >= len(self.data[0])
                or pos[1] < 0
                or pos[1] >= len(self.data)
            ):
                continue

            if pos in visited or pos in self.allVisited or pos in inLoop:
                continue

            if (
                pos[0] == 0
                or pos[0] == len(self.data[0]) - 1
                or pos[1] == 0
                or pos[1] == len(self.data) - 1
            ):
                if visited not in self._outerSets:
                    self._outerSets.append(visited)

            visited.add(pos)
            self.allVisited.add(pos)
            # Check up down left right
            for d in self._dirs:
                newPos = (pos[0] + d[0], pos[1] + d[1])
                q.append(newPos)

    def part2(self) -> int:
        values = {
            "|": 1,
            "-": 0,
            "L": 0.5,
            "J": 0.5,
            "7": 0.5,
            "F": 0.5,
        }

        inside = set()
        for y, row in enumerate(self.data):
            curRowParity = 0
            for x, sym in enumerate(row):
                if sym in values:
                    curRowParity += values[sym]
                elif sym == ".":
                    if curRowParity % 2 == 1:
                        inside.add((x, y))

        for y, row in enumerate(self.data):
            for x, sym in enumerate(row):
                if (x, y) in inside:
                    print("#", end="")
                elif (x, y) in self.getCellsInLoop():
                    print("X", end="")
                else:
                    print(".", end="")
            print()

        return len(inside)

        # Number of enclosed cells are the number of floodfill - number in loop
