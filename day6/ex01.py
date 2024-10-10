employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for emp in employees:
    total_earnings = emp[1] * emp[2]
    # total_earnings = round(total_earnings, 2)
    print(f"The total earnings {emp[0]} get paid is ${total_earnings:.2f}")
