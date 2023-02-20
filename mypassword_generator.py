import random

print("Welcome to the Password Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$*&().,'

number = input('Amount of passwords generated: ')
number = int(number)

length = input('Input your password within a certain length: ')
length = int(length)

print('\nThe following are generated passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
