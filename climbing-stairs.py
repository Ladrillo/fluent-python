def climbing_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a = 1
    b = 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


print(climbing_stairs(3))
