def is_palindrome(input_string):
    # Creamos dos cadenas para compararlas
    normal_string = input_string.replace(" ", "").lower()
    reverse_string = ""

    for letter in reversed(normal_string):
        reverse_string += letter

    # Comparamos las cadenas
    if normal_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Debería ser True
print(is_palindrome("abc"))  # Debería ser False
print(is_palindrome("kayak"))  # Debería ser True
