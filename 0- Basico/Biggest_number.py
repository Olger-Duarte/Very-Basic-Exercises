def biggest_number(numbers):
    
    biggest = 0

    for num in numbers:
        if num > biggest:
            biggest = num

    return biggest

numbers = [5, 7, 2, 4, 9, 1, 8]
print(bigger_number(numbers))  # debería imprimir 9


"""
def bigger_number(numbers):
    return max(numbers)

numbers = [5, 7, 2, 4, 9, 1, 8]
print(bigger_number(numbers))  # debería imprimir 9
"""