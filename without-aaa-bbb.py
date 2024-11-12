def strWithout3a3b(a, b):
    arrA = ["a" for _ in range(a)]
    arrB = ["b" for _ in range(b)]
    result = []
    print(arrA)
    print(arrB)
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) > len(arrB):
            result.append(arrA.pop())
            if len(arrA) > len(arrB):
                result.append(arrA.pop())
                continue
        if len(arrA) < len(arrB):
            result.append(arrB.pop())
            if len(arrA) < len(arrB):
                result.append(arrB.pop())
                continue
        else:
            result.append(arrA.pop())
            result.append(arrB.pop())
    return result


print(strWithout3a3b(3, 4))
