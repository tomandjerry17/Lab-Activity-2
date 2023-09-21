#Created by Martinez and Misajon

#enter personal details
fullName = input("Enter your full name: ")
idNum = input("Enter your ID Number: ")
Course = input("Enter your course   : ")
section = input("Enter your section  : ")
print()

#Grades
fq = eval(input("Enter your First Quarter Grade    : "))
sq = eval(input("Enter your Second Quarter Grade   : "))
tq = eval(input("Enter your Third Quarter Grade    : "))
fthq = eval(input("Enter your Fourth Quarter Grade   : "))
print("\n")

#formula
average = ((fq + sq + tq +fthq) / 4)

#display
print ("\n Full Name: ", fullName, "\n ID Number: ", idNum, "\n Course: ", Course, "\n Section: ", section)
print ("Your average grade is : " + str(average))


