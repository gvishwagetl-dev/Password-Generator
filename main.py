import random

def PasswordGenerator():
    #Writew your code here
    lower_characters = ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    upper_characters = ('A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    special_characters = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+')

    numerical_characters = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    password = random.choice(upper_characters) + random.choice(lower_characters) + random.choice(special_characters) + random.choice(numerical_characters) + random.choice(upper_characters) + random.choice(lower_characters) + random.choice(special_characters) + random.choice(numerical_characters)
   
    return password

print(PasswordGenerator())