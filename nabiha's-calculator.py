salary = float(input("Enter your salary for the month: "))

valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = input("Enter the month: ")
while month not in valid_months:
    print("Invalid month. Please enter a valid month name.")
    month = input("Enter the month: ")

def get_valid_percentage(prompt):
    while True:
        try:
            percentage = float(input(prompt))
            if 0 <= percentage <= 100:
                return percentage
            else:
                print("Please enter a valid percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

savings_percentage = get_valid_percentage("Enter the percentage for savings: ")
rent_percentage = get_valid_percentage("Enter the percentage for rent: ")
electricity_percentage = get_valid_percentage("Enter the percentage for electricity: ")

savings = (savings_percentage / 100) * salary 
rent = (rent_percentage / 100) * salary 
electricity = (electricity_percentage / 100) * salary

total_expense = savings + rent + electricity
remaining_salary = salary - total_expense

yearly_rent = rent * 12 
yearly_electricity = electricity * 12

salary_squared = salary ** 2

extra_savings = 50 
savings_divided = (extra_savings / savings) if savings != 0 else 0

print("\n--- Monthly Finance Report ---") 
print("Month: " + month) 
print("Savings: $" + str(savings)) 
print("Rent: $" + str(rent)) 
print("Electricity: $" + str(electricity)) 
print("Total Expenses: $" + str(total_expense)) 
print("Remaining Salary: $" + str(remaining_salary)) 
print("Yearly Rent Estimate: $" + str(yearly_rent)) 
print("Yearly Electricity Estimate: $" + str(yearly_electricity)) 
print("Salary Squared (Just for Fun): " + str(salary_squared)) 

