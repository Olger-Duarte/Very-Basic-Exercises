def fibonacci_recrusive(num):
    if num <= 1:
        return num
    return fibonacci_recrusive(num - 1) + fibonacci_recrusive(num - 2)

print(fibonacci_recrusive(6)) # Output: 8



def fibonacci_list(n):
    # Crear una lista para almacenar los valores de la secuencia de Fibonacci
    fibonacci = [0, 1]
    
    # Calcular los siguientes números de Fibonacci iterativamente
    for i in range(2, n + 1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    return fibonacci[n]

print(fibonacci_list(6))

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
   
    fib_prev = 0
    fib_current = 1
    
    # Calcular los siguientes términos de Fibonacci iterativamente
    for _ in range(2, n + 1):
        result = fib_prev + fib_current
        fib_prev = fib_current
        fib_current = result
    
    return fib_current

# Prueba de la función
print(fibonacci_iterative(6))

