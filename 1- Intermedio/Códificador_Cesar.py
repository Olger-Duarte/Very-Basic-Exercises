import random

alfa = [chr(i) for i in range(ord('a'), ord('z')+1)]
len_alfa = len(alfa)
cesar_key = random.randrange(3, 9)
codification_text = []

def codification(text):
    for letter in text:
        if not letter.isspace():
            position = (alfa.index(letter) + cesar_key) % len_alfa
            codification_text.append(alfa[position])
        else:
            codification_text.append(letter)
    
    return ''.join(codification_text)

print(f"Save the decodification Key: {cesar_key} \n")
print(codification(input("Enter text: ")))
