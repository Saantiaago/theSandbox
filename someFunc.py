def skobochki(string):
    hashmap = [0]*len(string)
    count = [0]*len(string)
    # for i in range(len(string)):
    #     count[i] += 1
    #     # if (hashmap[i] == string[i]):
    #     hashmap[i] = {string[i]: count[i]}
    #     print(hashmap[i])

    for i in range(len(string)):
        count[i] += 1
        newArr = [string[i], count[i]]
        hashmap[i] = newArr

        for j in range(i+1, len(string)):

            # print(hashmap.index(newArr[0] == string[j]))
            if newArr[0] == string[j]:
                newArr = [string[j], count[j]+1]
                hashmap[j] = newArr



    return(hashmap)