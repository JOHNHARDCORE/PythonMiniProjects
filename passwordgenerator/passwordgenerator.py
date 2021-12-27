import random
special_chars = '!@#$./,'

numbers = '1234567890'

letters = 'abcdefghijklmnopqrstuvwxyz'

password = []

# base pw: 32 chars, 1-8 special chars, 1-8 numbers, 1-8 uppercase, rest lower
# choose chars then shuffle 
# enjoy you are password
# generalize this l8r
# idk just do this in a loop l8r
remaining_chars = 32
num = random.randrange(1, 8)
remaining_chars -= num
chosen_letters = [random.choice(special_chars) for x in range(num)]

password.extend(chosen_letters)

num = random.randrange(1, 8)
remaining_chars -= num
chosen_letters = [random.choice(numbers) for x in range(num)]

password.extend(chosen_letters)

num = random.randrange(1, 12)
remaining_chars -= num
chosen_letters = [random.choice(letters).upper() for x in range(num)]

password.extend(chosen_letters)

chosen_letters = [random.choice(letters) for x in range(remaining_chars)]

password.extend(chosen_letters)
random.shuffle(password)
print("Your random password is:")
print(''.join(password)
