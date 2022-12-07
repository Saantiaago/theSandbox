import numbers


def order(sentence):
    # code here

    parsedSentence = sentence.split(" ")
    print(parsedSentence)
    resultSentence = [0] * len(parsedSentence)
    finalIndex = 0
    length = len(parsedSentence)

    for obj in range(length):
        for j in (parsedSentence[obj]):
            if j.isnumeric():
                finalIndex = int(j) - 1
                break
        resultSentence[finalIndex] = parsedSentence[obj]

    resultString = ''
    for i in range(len(resultSentence)):
        resultString += resultSentence[i]
        if i != len(resultSentence) - 1:
            resultString += ' '

    print(resultString)

    return resultString

