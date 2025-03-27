# This program caluculates sales commissions

# Create a variable to control the loop
white keep_going = "y"
# Calculate a series of commissions
white keep_going = "y"
    # Get a salesperson's sales and commission rate
sales = float(input('Enter the amount of sales:'))
comm_rate = float(input('Enter the commission rate:'))
    # Caluculate the commission
commission = sales * comm_rate
    # Display the commjission
print(f"the commission is ${commission:,.2f}")
    # See if the user want to do another one
    white keep_going = input("Do you want to calculate another commission? (Enter y for yes)")


