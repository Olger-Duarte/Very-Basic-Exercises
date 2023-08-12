def factorial(number):
    result = 1
    
    #Empieza en 2 ya que el factorial de 1 no tiene sentido
    for i in range(2, number + 1):
        result *= i   
    
    return result

number = int(input("Ingrese un número: "))
result = factorial(number)

print(f"El factorial de {number} es: {result}")
