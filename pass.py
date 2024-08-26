import random
import string
from random import shuffle

"""
characters = string.ascii_letters + string.digits + string.punctuation
num = int(input("Enter the length of the password: "))

for i in range(num):
    password = ''.join(random.choice(characters))
    print(password,end="")
"""
numbers = string.digits
symbols = string.punctuation
letters = string.ascii_letters

no_of_numbers = int(input("How many numbers do you need? "))
no_of_symbols = int(input("How many symbols do you need? "))
no_of_letters = int(input("How many letters do you need? "))

password = []

for i in range(1,no_of_numbers + 1):
    password += random.choice(numbers)
for i in range(1,no_of_symbols + 1):
    password += random.choice(symbols)
for i in range(1,no_of_letters + 1):
    password += random.choice(letters)

print(password)
random.shuffle(password)
new_pass = ""

for i in password:
    new_pass += i

print(new_pass)