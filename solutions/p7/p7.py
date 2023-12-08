import functools

import numpy as np

data = open("input.txt").read().split("\n")


values = "123456789TJQKA"


def getWinType(hand):
    freq = np.zeros(14)
    for card in hand:
        freq[values.index(card[0])] += 1

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


def evalHands(hand1, hand2):
    # Split into cards
    cards1 = hand1.split(" ")[0]
    cards2 = hand2.split(" ")[0]

    winType1 = getWinType(cards1)
    winType2 = getWinType(cards2)

    if winType1 < winType2:
        return 1
    elif winType1 > winType2:
        return -1

    # same win type
    # Go left to right, higher card wins
    for i in range(5):
        cardValue1 = values.index(cards1[i])
        cardValue2 = values.index(cards2[i])
        if cardValue1 < cardValue2:
            return 1
        elif cardValue1 > cardValue2:
            return -1

    return 0


def part1():
    sortedHands = sorted(data, key=functools.cmp_to_key(evalHands))

    s = 0
    for i, hand in enumerate(reversed(sortedHands)):
        bid = int(hand.split(" ")[1])
        s += bid * (i + 1)

    return s


def part2():
    pass


print(part1())
print(part2())
