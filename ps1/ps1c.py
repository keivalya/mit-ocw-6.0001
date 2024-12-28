starting_salary = int(input("Enter the starting salary: "))

semi_annual_raise = 0.07
total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
additional_return = 0

monthly_salary = annual_salary / 12
amount_saved = portion_saved * monthly_salary
amount_down_payment = portion_down_payment * total_cost

r = 0.04
months = 0

while current_savings < amount_down_payment:
    months += 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
    current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)
    print(f"Month: {months}, Current savings: {current_savings}, Additional return: {additional_return}")

print(f"Number of months: {months}")