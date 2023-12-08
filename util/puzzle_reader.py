def readPuzzle(fileName):
    data = open(fileName, "r").read().splitlines()
    data = [i for i in data if i != ""]
    return data


def readSample(fileName):
    data = readPuzzle(fileName)

    # Very last line is expected value
    expected = data[-1]

    # Make sure last line is just a number
    assert expected.isnumeric(), f"Expected value must be a number, got {expected}"

    data = data[:-1]

    return data, int(expected)
