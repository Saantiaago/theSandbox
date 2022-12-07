def duplicate_count(text):
    textDict = {}
    text = text.lower()

    for i in range(len(text)):
        textDict[text[i]] = text.count(text[i])

    print(textDict)
    count = 0

    for key in textDict:
        print(key)
        if textDict.get(key) > 1:
            count += 1

    print(count)
    return count


def sum_pairs(ints, s):
    resultArray = []

    for i in range(len(ints)):
        firstIndex = ints[i]
        for j in range(i + 1, len(ints)):
            secondIndex = ints[j]
            if firstIndex + secondIndex == s:
                if not resultArray:
                    resultArray.append(firstIndex)
                    resultArray.append(secondIndex)

    print(resultArray)
    if resultArray:
        return resultArray
    else:
        return None


def next_bigger(n):
    maxElement = -1
    newArr = [int(x) for x in str(n)]
    resultArr = []

    print(newArr)
    for j in range(len(newArr)):
        for i in range(len(newArr)):
            if newArr[i] > maxElement:
                maxElement = newArr[i]

        resultArr.append(maxElement)


# def is_solved(board):
    # TODO: Check if the board is solved!

    # if board[0][0]


    #
    # for i in range(len(board)):
    #     for j in range(len(board)):
    #         if (board[i]) () () () () ():
    #         print(board[i][j])


class A:

    @classmethod
    def lol(cls):
        pass
