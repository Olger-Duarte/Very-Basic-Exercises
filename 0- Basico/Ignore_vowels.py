user_word = input("Ingrese una palabra: ")
word_without_vowels = ""

for letter in user_word:
    if letter.upper() not in 'AEIOU':
        word_without_vowels += letter

print(word_without_vowels)
