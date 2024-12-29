starting_salary = int(input("Enter the starting salary: "))

epsilon = 100
semi_annual_raise = 0.07
total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
additional_return = 0

amount_down_payment = portion_down_payment * total_cost

r = 0.04
months = 0

high, low = 10000, 0
guess_portion_saved = (high + low) // 2
num_guesses = 0

while abs(current_savings - amount_down_payment) > epsilon:
    current_savings = 0
    monthly_salary = starting_salary / 12
    guess_portion_saved = (high + low) // 2
    for i in range(36):
        current_savings += (current_savings * r / 12) + (guess_portion_saved/10000 * monthly_salary)
        if i % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    if current_savings < amount_down_payment:
        low = guess_portion_saved
    else:
        high = guess_portion_saved
    if high-1 == low: print("It is not possible to pay the down payment in three years."); exit()
    print(f"Current savings: {current_savings}, High: {high}, Low: {low}")
    num_guesses += 1

print(f"Best savings rate: {guess_portion_saved / 10000}")
print(f"Steps in bisection search: {num_guesses}")