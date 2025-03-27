# Get a number of seconds from user. Calculate hours, minutes, and seconds.
#print(f"{5 // 2}") 2
#print(f"{5 % 2}") 1


# Enter your seconds: 7877
# That is xx hours xx minustes and xx seconds


total_seconds = int(input("Please enter the seconds: "))
# Calculate hours
hours = total_seconds // 3600
# Calculate remaining minustes
minutes = (total_seconds // 60) % 60
# Get the remaining seconds
seconds = total_seconds % 60
# Display the result
print('Here is the time in hours, minutes, and seconds:')
print('Hours: ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds)

