# This function calculates the money remaining
# for an employee after taxes and expenses.

def savings():
    print("Welcome to Money After Tax and Expenses Calculator!\n")
    name = input("Enter Employee's Full Name: ")
    gross_pay = int(input("Enter Income: "))
    expenses = int(input("Enter Expenses: "))
    tax_rate = float()
    if gross_pay <= 250000:
        tax_rate = gross_pay * .0
    elif gross_pay <= 400000:
        tax_rate = gross_pay * .15
    elif gross_pay <= 800000:
        tax_rate = gross_pay * .20 + 22500
    elif gross_pay <= 2000000:
        tax_rate = gross_pay * .25 + 102500
    elif gross_pay <= 8000000:
        tax_rate = gross_pay * .30 + 402500
    else:
        tax_rate = gross_pay * .35 + 2205500

    total_savings = gross_pay - tax_rate - expenses

    print("\nEmployee Name:", name, "\nAfter Tax Savings Report:\n")
    print("taxes amounted ₱", tax_rate, "in taxes.")
    print("Your expenses amounted to ₱", expenses)
    print("You saved ₱", total_savings, "after taxes and expenses.")


savings()
