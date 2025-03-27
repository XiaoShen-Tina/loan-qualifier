# Based on students score, we will give litter grade. Use the follwing schema.
#A_SCORE = 90
#SCORE = 70
#D_SCORE = 60
#< 60 F

A = 90
B = 80
C = 70
D = 60

#Get a score
score = int(input("Enter your score:"))
# Determine 
if score >= A:
    print("You got A")
else:
    if score >= B:
        print("You got B")
    else:
        if score >= C:
            print("You got C")
        else:
             if score >= D:
                print("You got D")
             else:
                 print("You got F")