import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Easy level PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
# for letter in range(0, num_letters):
#     password += random.choice(letters)
#
# for symbol in range(0, num_symbols):
#     password += random.choice(symbols)
#
# for number in range(0, num_numbers):
#     password += random.choice(numbers)
#
# print(password)



print("Welcome to the Hard level Pypassword Generator!")
password = []
for letter in range(0, num_letters):
    password.append(random.choice(letters))

for symbol in range(0, num_symbols):
    password.append(random.choice(symbols))

for number in range(0, num_numbers):
    password.append(random.choice(numbers))
print(password)
print(random.shuffle(password))
empty_password = ""
converted_password = empty_password.join(password)
print(converted_password)