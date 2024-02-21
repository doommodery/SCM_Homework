def calculate_interest_rate(principal, final_amount, years):
    interest_rate = ((final_amount / principal) ** (1/years) - 1) * 100
    return interest_rate

principal = float(input("Введите первоначальную сумму: "))
final_amount = float(input("Введите итоговую сумму: "))
years = int(input("Введите срок вклада в годах: "))

interest_rate = calculate_interest_rate(principal, final_amount, years)
print(f"Годовая процентная ставка равна {interest_rate:.2f}%")