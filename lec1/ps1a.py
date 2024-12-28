# annual_salary = int(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = int(input("Enter the cost of your dream home: "))

annual_salary = 120000
portion_saved = .10
total_cost = 1000000

portion_down_payment = 0.25
current_savings = 0
additional_return = 0

amount_saved = portion_saved * annual_salary / 12
amount_down_payment = portion_down_payment * total_cost

r = 0.04
months = 1

while current_savings < amount_down_payment:
    additional_return += current_savings * r / 12
    amount_saved += amount_saved / 12
    current_savings += additional_return + amount_saved
    months += 1

print(f"Number of months: {months}")