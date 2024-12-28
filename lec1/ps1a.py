annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
additional_return = 0

monthly_salary = annual_salary / 12
amount_saved = portion_saved * monthly_salary
amount_down_payment = portion_down_payment * total_cost

r = 0.04
months = 0

while current_savings < amount_down_payment:
    current_savings += (current_savings * r / 12) + amount_saved
    months += 1
    print(f"Month: {months}, Current savings: {current_savings}, Additional return: {additional_return}")

print(f"Number of months: {months}")