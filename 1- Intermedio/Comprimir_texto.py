def compress(string):
    compressed = ''
    count_dict = {}

    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    for char, count in count_dict.items():
        compressed += char + str(count)

    return compressed if len(compressed) < len(string) else string

result = compress(input("Ingrese un string: "))
print("Resultado:", result)
                                            