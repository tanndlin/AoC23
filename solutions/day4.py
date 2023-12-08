from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def parseCard(self, card):
        card = card.replace("   ", " ")
        card = card.replace("  ", " ")
        temp = card.split(": ")
        id = int(temp[0].split(" ")[1])

        temp = temp[1].split(" | ")
        winningNumbers = [int(x) for x in temp[0].split(" ")]
        currentNumbers = [int(x) for x in temp[1].split(" ")]

        return id, winningNumbers, currentNumbers

    def getNumMatches(self, winningNumbers, currentNumbers):
        matches = 0
        for cur in currentNumbers:
            if cur in winningNumbers:
                matches += 1

        return matches

    def getCardValue(self, card):
        id, winningNumbers, currentNumbers = self.parseCard(card)
        matches = self.getNumMatches(winningNumbers, currentNumbers)

        if matches == 0:
            return 0

        return 2 ** (matches - 1)

    def part1(self):
        s = 0
        for card in self.data:
            s += self.getCardValue(card)

        return s

    def part2(
        self,
    ):
        cards = {}
        s = 0
        copies = {i: 1 for i in range(1, len(self.data) + 1)}
        for card in self.data:
            id, winningNumbers, currentNumbers = self.parseCard(card)
            matches = self.getNumMatches(winningNumbers, currentNumbers)
            cards[id] = matches

            if matches == 0:
                continue

            for i in range(id + 1, id + matches + 1):
                copies[i] += 1 * copies[id]

        return sum(copies.values())
