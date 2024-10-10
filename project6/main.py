for n in range(1, 101):
    # if number % 15 == 0:
    #     print("Fizz Buzz")
    # elif number % 5 == 0:
    #     print("Buzz")
    # elif number % 3 == 0:
    #     print("Fizz")
    # else:
    #     print(number)
    print('Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or n)
