def isEven(number):
    if number % 2 == 0:
        return str(number) + " es un número par"
    else:
        return str(number) + " es un número impar"


number = 4
print(isEven(number))
