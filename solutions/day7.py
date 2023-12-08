import functools

import numpy as np

from util.solution_base import SolutionBase

# values = "123456789TJQKA"


class Solution(SolutionBase):
    def __init__(self, _data, expectedValue=-1):
        super().__init__(_data, expectedValue)
        for i in range(len(self.data)):
            self.data[i] = self.data[i].split(" ")
            self.data[i] = {"cards": self.data[i][0], "bid": int(self.data[i][1])}

    def getWinType(self, hand):
        freq = np.zeros(14)
        for card in hand:
            freq[self.values.index(card[0])] += 1

        if 5 in freq:
            return 6

        if 4 in freq:
            return 5

        if 3 in freq and 2 in freq:
            return 4

        if 3 in freq:
            return 3

        # 2 pairs
        if np.count_nonzero(freq == 2) == 2:
            return 2

        # 1 pair
        if 2 in freq:
            return 1

        return 0

    def evalCards(self, cards1, cards2):
        winType1 = self.getWinType(cards1)
        winType2 = self.getWinType(cards2)

        if winType1 < winType2:
            return 1
        elif winType1 > winType2:
            return -1

        # same win type
        # Go left to right, higher card wins
        for i in range(5):
            cardValue1 = self.values.index(cards1[i])
            cardValue2 = self.values.index(cards2[i])
            if cardValue1 < cardValue2:
                return 1
            elif cardValue1 > cardValue2:
                return -1

        return 0

    def evalHands(self, hand1, hand2):
        # Split into cards
        cards1 = hand1["cards"]
        cards2 = hand2["cards"]

        evalCardsResult = 0
        if self.wildCard:
            evalCardsResult = self.evalCards(
                self.makeStrongestHand(cards1), self.makeStrongestHand(cards2)
            )
        else:
            evalCardsResult = self.evalCards(cards1, cards2)
        if evalCardsResult != 0:
            return evalCardsResult

        # Go left to right, higher card wins
        for i in range(5):
            cardValue1 = self.values.index(cards1[i])
            cardValue2 = self.values.index(cards2[i])
            if cardValue1 < cardValue2:
                return 1
            elif cardValue1 > cardValue2:
                return -1

        return 0

    def part1(self):
        self.wildCard = False
        self.values = "123456789TJQKA"
        sortedHands = sorted(self.data, key=functools.cmp_to_key(self.evalHands))

        s = 0
        for i, hand in enumerate(reversed(sortedHands)):
            s += hand["bid"] * (i + 1)

        return s

    def getAllPossibleHands(self, cards):
        if "J" not in cards:
            yield cards
            return

        # This hand contains at least one Joker
        for v in self.values:
            if v == "J":
                continue
            yield from self.getAllPossibleHands(cards.replace("J", v, 1))

    @functools.lru_cache(maxsize=None)
    def makeStrongestHand(self, cards) -> str:
        if cards == "JJJJJ":
            return "AAAAA"
        if cards.count("J") == 4:
            # Make all 4 the same as the 5th
            for v in self.values:
                if v != "J":
                    return cards.replace("J", v)

        hands = self.getAllPossibleHands(cards)
        return min(hands, key=functools.cmp_to_key(self.evalCards))

    def part2(self):
        self.values = "J123456789TQKA"
        self.wildCard = True
        sortedHands = sorted(self.data, key=functools.cmp_to_key(self.evalHands))

        s = 0
        for i, hand in enumerate(reversed(sortedHands)):
            bid = hand["bid"]
            s += bid * (i + 1)

        return s
