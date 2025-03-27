# Get the desired future value
future_value = float(input("Enter the amount of money you want to make: "))
# Get the annual interest rate
rate = float(input("Enter the annual interest rate: "))
# Get the number of years that the money will appreciate
years = int(input("Enter the year the money will grow:"))
# Calculate the amount needed to depoit
present_value = future_value / (1.0 + rate**years)
# Display the amount needed to deposit
print(f"If you want to make {future_value:,.2f} yuan with annual interest rate as {rate:.0%}, in {years} years, you need yo desposit today {present_value:,.2f}")