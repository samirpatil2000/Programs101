def fun(n):
    binary_string = bin(n)[2:]
    result = []
    for i in range(len(binary_string)):
        if binary_string[i] == "1":
            result.append(i + 1)
    return [len(result)] + result

print(fun(1))
    