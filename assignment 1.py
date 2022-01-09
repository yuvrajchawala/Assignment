#Question 1
#input three numbers
x=int(input("ENTER FIRST NUMBER: "))
y=int(input("ENTER SECOND NUMBER: "))
z=int(input("ENTER THIRD NUMBER: "))
#to print average
print("The average of three numbers is: ",(x+y+z)/3)

print("********************************************************")

#Question 2
#Asking for gross income and no. of dependents
x=float(input("ENTER YOUR INCOME: "))
y=int(input("ENTER NUMBER OF DEPENDENTS: "))
#To calculate taxable income and tax
z=x-10000-(y*3000)
tax=z*20/100
#To print tax and taxable income
print("Your taxable income is: ",z)
print("Your tax amount is: ",tax)

print('**********************************************************')

#Question 3
#To input the data from student
SID=int(input("ENTER YOUR STUDENT ID: "))
NAME=str(input("ENTER YOUR NAME: "))
GENDER=str(input("ENTER F FOR FEMALE AND M FOR MALE AND U FOR UNKNOWN: "))
COURSE=str(input("ENTER COURSE NAME: "))
CGPA=float(input("ENTER YOUR CGPA: "))
#TO create list
STUDENT=[SID,NAME,GENDER,COURSE,CGPA]
#to print list
print(STUDENT)

print("**************************************************************")

#Question 4
#To enter marks of 5 students
x=int(input("ENTER FIRST STUDENT MARKS: "))
y=int(input("ENTER SECOND STUDENT MARKS: "))
z=int(input("ENTER THIRD STUDENT MARKS: "))
a=int(input("ENTER FOURTH STUDENT MARKS: "))
b=int(input("ENTER FIFTH STUDENT MARKS: "))
#To create and sort list
p=[x,y,z,a,b]
p.sort()
#Print the list
print(p)

print("*****************************************************************")

#Question 5
#To enter list
color=['Red','Green','White','Black','Pink','Yellow']
#Create a copy of list for next part of question
z=color.copy()
#To remove the 4th element and print the list
color.pop(3)
print(color)
#To replace 'Black' and "Pink" with "Purple"
z[3]="Purple"
z[4]="Purple"
#To print the answer
print(z)

