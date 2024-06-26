import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

should_continue = True
while should_continue:
    nr_letters = 3
    nr_numbers = random.randint(1, 2)
    nr_symbols = random.randint(0, 1)
    
    password_list = []
    
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))
    
    random.shuffle(password_list)
    
    password = "".join(password_list)
    print(f"Password generated is: {password}")
    
    enter = input("Enter the password: ")
    
    if password == enter:
        print("Password correct.")
        should_continue = False
    else:
        print("Password incorrect. Try again.")
