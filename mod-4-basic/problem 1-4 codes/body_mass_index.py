print("Welcome to BMI Calculator!")
name = input("\nEnter your First Name here: ")
weight = float(input("Enter your Weight in Kilogram here: "))
height = float(input("Enter your Height in Meter here: "))


def body_mass_index(weight, height):
    bmi = weight / height ** 2
    return bmi


bmi_result = body_mass_index(weight, height)
print(f"{name}, your BMI is: {bmi_result:.2f}")
print("\nFor reference:")
print("\nBMI < 18.5 = underweight \nBMI < 25 = normal \nBMI < 30 = overweight \nBMI > 30 = Obese")
