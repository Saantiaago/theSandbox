def accum(s):
    resultStr = ""
    count = 0

    for el in s:
        resultStr += el.capitalize()
        for i in range(count):
            resultStr += el.lower()
        count += 1
        if count < len(s):
            resultStr += "-"

    print(resultStr)

