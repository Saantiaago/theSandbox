

def anagrams(word, words):
    letterDict = {}
    for i in range(len(word)):
        letterDict[word[i]] = word.count(word[i])

    print(letterDict)
    resultArray = []

    for element in words:
        tempDict = {}
        for i in range(len(element)):
            tempDict[element[i]] = element.count(element[i])
        print(tempDict)
        if letterDict == tempDict:
            print('yees')
            resultArray.append(element)

    print(resultArray)
    return resultArray


