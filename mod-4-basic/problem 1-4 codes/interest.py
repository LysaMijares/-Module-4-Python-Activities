def interest(principal, rate, periods):
    simple_interest = principal * (rate * periods)
    return principal + simple_interest


principal = int(input("Enter the principal:"))
rate = float(input("Enter the rate:"))
periods = int(input("Enter the number of periods invested:"))

final_value = interest(principal, rate, periods)
print(f"The final value of the investment is: {final_value:.2f}")

