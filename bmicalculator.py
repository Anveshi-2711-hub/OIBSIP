def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()
