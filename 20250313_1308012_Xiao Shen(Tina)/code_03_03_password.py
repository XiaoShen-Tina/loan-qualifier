# This program compares two strings and if the pair of the string is match then show greeting otherwise kick out
# Set password
password = "134680"
# Get input of password
inp_password = input("Plese enter the password:")
# If the inputed password is same to password that you set then show greeting message
if inp_password == password:
    print("Hello, good to see you again")
# Otherwise shows bye-bye message
else:
    print("Sorry, wrong password, bye bye until enter right password")