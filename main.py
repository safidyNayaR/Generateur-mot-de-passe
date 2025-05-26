import random
import string

def generate_password(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    character = letters
    if numbers:
        character += digits
    if special_char:
        character += punctuation

    pwd = ""
    meets_resp = False
    has_number = False
    has_special = False

    while not meets_resp or len(pwd) < min_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in punctuation:
            has_special = True

        meets_resp = True
        if numbers:
            meets_resp = has_number
        if special_char:
            meets_resp = meets_resp and has_special
    return pwd

min_length = int(input("Entrer la longuer minimale du mot de passe: "))
numbers_ok = input("Voulez-vous des nombres ? (y/n): ").lower() == 'y'
special_ok = input("Voulez-vous des caractères spéciaux ? (y/n): ").lower() == 'y'

print(generate_password(min_length, numbers_ok, special_ok))