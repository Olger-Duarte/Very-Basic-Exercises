def bubble_sort(numbers):
    quantity_numbers = len(numbers)
    
    # Iteramos cantidad_elementos veces por la lista
    for actual_position in range(quantity_numbers):
        # Iteramos de 0 a cantidad_elementos - actual_position - 1, porque los últimos
        # actual_position elementos ya están ordenados
        for actual_number in range(0, quantity_numbers - actual_position - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if numbers[actual_number] > numbers[actual_number+1]:
                numbers[actual_number], numbers[actual_number+1] = numbers[actual_number+1], numbers[actual_number]

    return numbers

numbers = [5, 2, 8, 3, 1]
print(bubble_sort(numbers))  # Output: [1, 2, 3, 5, 8]
