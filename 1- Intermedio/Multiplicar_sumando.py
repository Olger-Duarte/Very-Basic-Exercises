def multiply(*args):
    result = 1
    values = list(map(abs, args))

    for value in values:
        product = result
        for _ in range(value-1):
            result += product

    return -result if any(num < 0 for num in args) else result

print(multiply(-2, 3)) # Output: -6
print(multiply(2, 3, 4)) # Output: 24
