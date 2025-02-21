salary = float(input("Enter your salary for the month: "))

valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = input("Enter the month: ")
while month not in valid_months:
    print("Invalid month. Please enter a valid month name.")
    month = input("Enter the month: ")

