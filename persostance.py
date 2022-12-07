def persistence(n):
    result = 1
    count = 0
    for i in str(n):
        result *= int(i)

    if n / 10 >= 1:
        count += 1
    else:
        return 0

    while result / 10 >= 1:
        subRes = result
        result = 1
        for i in str(subRes):
            result *= int(i)
        count += 1
    print(count)
    return(count)

    # your code
