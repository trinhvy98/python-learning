name = input("enter your name: ")
hourly_wage = float(input("enter your hourly wage: "))

hours_worked = float(input("enter hours worked: "))

employee_name = name.strip().title()

print(f"Employee's name: {employee_name}")
total_earnings = hourly_wage * hours_worked

print(f"your total earnings: {total_earnings:.2f}$")
