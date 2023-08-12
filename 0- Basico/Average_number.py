def calculateAverage(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(calculateAverage(numbers)) # Output: 3.0