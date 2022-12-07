def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def dig_pow(n, p):
    # your code
    totalSum = 0
    arrayOfInt = [0]*len(str(n))

    for i in range(len(str(n))):
        arrayOfInt[i] = str(n)[i]

    for i in range(len(arrayOfInt)):
        subSum = int(arrayOfInt[i])**p
        totalSum += subSum
        p += 1
        subSum = 0

    k = totalSum / n

    print(int(k))
    print(k - int(toFixed(k)))

    if k - float(toFixed(k)) == 0:
        print(int(k))
        return k
    else:
        return -1
