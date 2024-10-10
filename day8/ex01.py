import random
magic_number = random.randint(1, 100)

while True:
    guess = int(input("enter a number: "))
    if guess>magic_number:
        print("too high")
    elif guess<magic_number:
        print("too low")
    else:
        print("correctly")
        break
