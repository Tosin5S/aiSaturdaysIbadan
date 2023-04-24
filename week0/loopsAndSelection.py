# Repitition (Loops) and Selection (if/else)
# It is part of the core aspect

# if (condition):
   # statement:

gpa = 3.142

if (gpa > 2.5):
    print("Your class of degree is above 2.2")

else: 
    print("Your class of degree is ...")

print ("DISPLAY STUDENT CLASS OF DEGREE")

cgpa = float(input("Enter your cgpa: "))
if (cgpa >= 4.5):
    print("You are a first class student")
elif((cgpa >= 3.5) and (cgpa < 4.5)):
    print("You are a second class upper student")
elif((cgpa >= 2.5) and (cgpa < 3.49)):
    print("You are a second class lower student")
elif((cgpa >= 1.5) and (cgpa < 2.49)):
    print("You are a third class student")
else:
    print("You will have to go to your house (lol)")

###################################################
# Control Structures or Repetitive Statements

x = 1
while (x <= 100):
    print (x)
    x = x + 1

# Even numbers between 1 to 100

x = 2
while (x <= 100):
    print (x)
    x = x + 2

# assignment 1: print prime numbers between 1 and 100
# assignment 2: calculate n factorial
# assignment 3: use math.pi to calculate the volume of a cone
