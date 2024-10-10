card_number = list(input("pls enter ur card number: ").strip())
checking_digit = card_number.pop()
card_number.reverse()

card_number_digit = []

for index, digit in enumerate(card_number):
    num = int(digit)

    if index % 2 == 0:
        num *= 2
        if num > 9:
            num -= 9
    card_number_digit.append(num)

total = int(checking_digit) + sum(card_number_digit)
# if total % 10 == 0:
#     print("valid")
# else:
#     print("invalid")
print("Valid" if total % 10 == 0 else "Invalid")
