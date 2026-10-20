import random
secret_numbers= random.randint(1, 10)
while True:
    guess= int(input('choose the number 1 to 10: '))
    if guess > secret_numbers:
        print('Too high')
    elif guess < secret_numbers:
        print('Too low')
    else:
        print('Correct')
        break 