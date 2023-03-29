# This function calculates how much material input will be wasted
# after running a certain number of jobs that consume

def material_waste():
    print("Welcome to Material Waste Calculator!")
    total_material = int(input("Enter the Total Material Available: "))
    material_units = str(input("Kilogram, or Liter? (kg or L): "))
    num_jobs = int(input("Enter Number of Jobs Available:"))
    job_consumption = int(input("Enter the Material Consumption per Job:"))
    material_c = int()
    total_consumption = int()

    if material_units == "kg":
        material_units = "Kgs"
    elif material_units == "L":
        material_units = "L"
    else:
        print("Invalid Weight unit!")

    material_c = num_jobs * job_consumption
    total_consumption = material_c

    print("Total Material: ", total_material, f"{material_units}")
    print("Total Material Consumption:", total_consumption, f"{material_units}")


material_waste()
