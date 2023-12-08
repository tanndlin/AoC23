def readPuzzle(fileName):
    data = open(fileName, "r").read().splitlines()
    data = [i for i in data if i != ""]
    return data


def readSample(fileName):
    data = readPuzzle(fileName)

    # Second to last is expected for part 1
    expected1 = data[-2]

    # Very last line is expected for part 2
    expected2 = data[-1]

    # Make sure last two lines are just numbers
    assert expected1.isnumeric(), f"Expected value must be a number, got {expected1}"

    # May have not unlocked the second part yet
    # assert expected2.isnumeric(), f"Expected value must be a number, got {expected2}"

    data = data[:-2]

    return data, int(expected1), int(expected2)
