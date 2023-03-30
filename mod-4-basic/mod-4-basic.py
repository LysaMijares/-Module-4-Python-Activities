'''Module 2: Individual Programming Assignment 1
Useful Business Calculations
This assignment covers your basic proficiency with Python.
'''


def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.
    This function calculates the money remaining
        for an employee after taxes and expenses.

    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee
    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos
    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''

    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Answer
    def savings():
        print("Welcome to Money After Tax and Expenses Calculator!\n")
        # inputs the required data into the program
        name = input("Enter Employee's Full Name: ")
        gross_pay = int(input("Enter Income: "))
        expenses = int(input("Enter Expenses: "))
        tax_rate = float() # this could turn into tax_rate = float(input()) to have personalized tax_rate
        # tax rate used is Philippines Taxes on personal income
        # converts the tax rate by using gross_pay and multiplying it to the indicated tax rate in the taxable income
        # bracket
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
            # total saving can be acquired by subtracting tax_rate and expenses to the gross_pay
        total_savings = gross_pay - tax_rate - expenses
        # prints the tax report
        print("\nEmployee Name:", name, "\nAfter Tax Savings Report:\n")
        print("taxes amounted ₱", tax_rate, "in taxes.")
        print("Your expenses amounted to ₱", expenses)
        print("You saved ₱", total_savings, "after taxes and expenses.")

    savings()


def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.
    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.
    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.
    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.
    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job
    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''

    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Answer
    def material_waste():
        print("Welcome to Material Waste Calculator!")
        # inputs the required int and strings to the program
        total_material = int(input("Enter the Total Material Available: "))
        material_units = str(input("Kilogram, or Liter? (kg or L): "))
        num_jobs = int(input("Enter Number of Jobs Available:"))
        job_consumption = int(input("Enter the Material Consumption per Job:"))
        material_c = int()
        total_consumption = int()
        # strings for material units for kilogram and liter (Kgs, L)
        if material_units == "kg":
            material_units = "Kgs"
        elif material_units == "L":
            material_units = "L"
        else:
            print("Invalid Weight unit!")
        # converts the material consumption by multiplying num_jobs to the job_consumption
        material_c = num_jobs * job_consumption
        total_consumption = material_c
        # prints the material consumption
        print("Total Material: ", total_material, f"{material_units}")
        print("Total Material Consumption:", total_consumption, f"{material_units}")

    material_waste()


def interest(principal, rate, periods):
    '''Interest.
    3 points.
    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.
    To calculate simple interest, simply multiply the principal to the quantity (rate * time).
        Add this amount to the principal to get the final value.
    Round down the final amount.
    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested
    Returns
    -------
    int
        the final value of the investment
    '''

    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Answer
    def interest(principal, rate, periods):
        simple_interest = principal * (rate * periods)
        return principal + simple_interest
    # inputs the required data here
    principal = int(input("Enter the principal:"))
    rate = float(input("Enter the rate:"))
    periods = int(input("Enter the number of periods invested:"))

    final_value = interest(principal, rate, periods)
    # prints the value of the investment
    print(f"The final value of the investment is: {final_value:.2f}")


def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.
    This function calculates the body mass index (BMI) of a person
        given their weight and height.
    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)
    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.

    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].
    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Answer
    print("Welcome to BMI Calculator!")
    # inputs the required data into the program
    name = input("\nEnter your First Name here: ")
    weight = float(input("Enter your Weight in Kilogram here: "))
    height = float(input("Enter your Height in Meter here: "))

    def body_mass_index(weight, height):
        # operation to be made in getting BMI
        bmi = weight / height ** 2
        return bmi

    bmi_result = body_mass_index(weight, height)
    # prints the name and the BMI result
    print(f"{name}, your BMI is: {bmi_result:.2f}")
    print("\nFor reference:")
    print("\nBMI < 18.5 = underweight \nBMI < 25 = normal \nBMI < 30 = overweight \nBMI > 30 = Obese")



