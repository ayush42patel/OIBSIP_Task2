def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_user_input():
    weight = float(input("Enter your weight in kilograms (e.g., 70.5): "))
    height = float(input("Enter your height in meters (e.g., 1.75): "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
        exit()
        
    return weight, height

print("=== BMI Calculator ===")
weight, height = get_user_input()

if weight is None or height is None:
    print("Program exited due to invalid input.")
    
bmi = calculate_bmi(weight, height)
category = categorize_bmi(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")