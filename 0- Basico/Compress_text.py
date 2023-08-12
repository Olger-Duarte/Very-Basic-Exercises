def compress(texto="aabbbcccc"):
    compressed = ''
    count = 1

    for i in range(len(texto)):
        if i < len(texto) - 1 and texto[i] == texto[i + 1]:
            count += 1
        else:
            compressed += texto[i] + str(count)
            count = 1

    return compressed if len(compressed) < len(texto) else texto

resultado = compress(input("Ingresa el texto: "))
print(resultado)
