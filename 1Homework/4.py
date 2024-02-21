def calculate_deposit_amount(principal, interest_rate, years):
    daily_interest_rate = interest_rate / 365
    total = principal * (1 + daily_interest_rate) ** (365 * years)
    return total

principal = float(input("Введите первоначальную сумму: "))
interest_rate = float(input("Введите годовую процентную ставку (в десятичной дроби): "))
years = int(input("Введите срок вклада в годах: "))

final_amount = calculate_deposit_amount(principal, interest_rate, years)
print("Итоговая сумма депозита: {}".format("{:.2f}".format(final_amount)))