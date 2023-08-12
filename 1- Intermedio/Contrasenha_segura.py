import string
import random

letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
chars = list(filter(lambda char: not char.isalnum(), string.printable))

def password(pass_size):
    result_password = ""
    for _ in range(int(pass_size)):
        chooosen =  random.randrange(0, 3)
        match chooosen:
            case 0:
                result_password += random.choice(letters)
            case 1:
                result_password += random.choice(chars)
            case 2:
                result_password += str(random.randrange(0, 9))
    return result_password

pass_length = input('Insert password size: ')
print(f"Final password: {password(pass_length)} \n")
