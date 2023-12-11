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

    def part1(self) -> int:
        self.preprocess()
        print(self.adj[self.start])

        queue = [self.start]
        visited = set()

        while len(queue) > 0:
            pos = queue.pop(0)

            if pos in visited:
                continue

            visited.add(pos)
            queue.extend(self.adj[pos])

        return len(visited) // 2
