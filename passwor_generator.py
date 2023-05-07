import random
import string


def generate_password(min_lenght , numbers =True , special_charcters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters 
    if numbers :
        characters += digits
    if special_charcters:
        characters += special    

    pwd =""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits :
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_charcters :
            meets_criteria = meets_criteria and has_special
    
    
    return pwd

min_lenght = int(input("Podaj mininamlna dlugośc hasla  "))
has_number = (input("Chcesz liczby (y/n)")).lower() == "y"
has_special = input("Chcesz specialne znaki (y/n)").lower() == "y"

haslo = generate_password(min_lenght, has_number ,has_special)
print ("Wygernerowaner haslo to ", haslo)
