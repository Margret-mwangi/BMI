from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    age = current_year - birth_year
    return age

# Example usage
birth_year_input = int(input("Enter your birth year: "))
age = calculate_age(birth_year_input)
print(f"You are {age} years old.")