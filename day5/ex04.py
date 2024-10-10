employee_worked_hours = float(input("enter the worked hours: "))
employee_hourly_wage = float(input("enter the hourly wage: "))

total_earnings = employee_hourly_wage * employee_worked_hours

if employee_worked_hours > 40:
    overtime = (employee_worked_hours - 40) * employee_hourly_wage * 1.1
    regular_earnings = 40 * employee_hourly_wage
    total_earnings = overtime + regular_earnings
print(total_earnings)
