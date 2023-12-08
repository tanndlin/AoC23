import functools

import numpy as np

from util.solution_base import SolutionBase


class Solution(SolutionBase):
    def preprocess(self):
        for i in range(len(self.data)):
            self.data[i] = self.data[i].split(" ")
            self.data[i] = {"cards": self.data[i][0], "bid": int(self.data[i][1])}

    @functools.lru_cache(maxsize=None)
    def getWinType(self, hand):
        freq = np.zeros(13)
        for card in hand:
            freq[self.values[card]] += 1

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

    def evalCards(self, cards1, cards2, breakTie=True):
        winType1 = self.getWinType(cards1)
        winType2 = self.getWinType(cards2)

        if winType1 < winType2:
            return 1
        elif winType1 > winType2:
            return -1

        if not breakTie:
            return 0

        # same win type
        # Go left to right, higher card wins
        for i in range(5):
            cardValue1 = self.values[cards1[i]]
            cardValue2 = self.values[cards2[i]]
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

        cardToEval1 = cards1 if not self.wildCard else self.makeStrongestHand(cards1)
        cardToEval2 = cards2 if not self.wildCard else self.makeStrongestHand(cards2)

        print("to eval")
        print(cardToEval1, cardToEval2)

        evalCardsResult = self.evalCards(cardToEval1, cardToEval2, breakTie=False)
        if evalCardsResult != 0:
            print("WINNER", evalCardsResult)
            print(cards1, cards2)

            return evalCardsResult

        print("TIE")
        # Go left to right, higher card wins
        # Using the original cards, instead of the Jokers
        for i in range(5):
            cardValue1 = self.values[cards1[i]]
            cardValue2 = self.values[cards2[i]]
            if cardValue1 < cardValue2:
                print(1)
                return 1
            elif cardValue1 > cardValue2:
                print(-1)
                return -1

        print(0)

        return 0

    def getFinalScore(self, hands):
        s = 0
        for i, hand in enumerate(reversed(hands)):
            s += hand["bid"] * (i + 1)

        return s

    def part1(self):
        self.wildCard = False
        self.values = {k: i for i, k in enumerate("23456789TJQKA")}
        sortedHands = sorted(self.data, key=functools.cmp_to_key(self.evalHands))

        return self.getFinalScore(sortedHands)

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
        self.values = {k: i for i, k in enumerate("J23456789TQKA")}
        self.wildCard = True
        sortedHands = sorted(self.data, key=functools.cmp_to_key(self.evalHands))
        for i in sortedHands:
            print(i)

        print(self.getWinType("2JJJJ"))
        print(self.getWinType("JAAAA"))
        print(self.evalHands({"cards": "2JJJJ"}, {"cards": "JAAAA"}))

        return self.getFinalScore(sortedHands)
