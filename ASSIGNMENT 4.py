#Question 1
def towerofhanoi(n,source,destination,auxillary):
    if(n==1):
        print("Move disk 1 from source",source,"to destination",destination)
        return
    towerofhanoi(n-1,source,auxillary,destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    towerofhanoi(n-1,auxillary,destination,source)
towerofhanoi(3,'A','B','C')

print("\n********************************************************************************************************************************\n")

print("\nQuestion 2")

#Question 2
n=int(input("Enter the no. rows:"))
#Using recursion
print("\nUSING RECURSION\n")
def pascaltriangle(num):
    if num == 1:                                                        
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                      
        current_row = [1]                                       
        previous_row = result[-1]                       
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]                                  
        result.append(current_row)                  
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")                    
    for j in i:
        print(j, end =" ")
    print()

#Using Iteration
print("\nUSING ITERATION\n")
from math import factorial
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()

print("\n********************************************************************************************************************************\n")

print("\nQuestion 3")

#Question 3
number_1=int(input("Enter the first integer:"))
number_2=int(input("Enter the second integer:"))
if(number_2!=0):
   quotient,modulous=divmod(number_1,number_2)
   print("The quotient is:",quotient)
   print("The modulous is:",modulous)
   call=callable(divmod)
   if(call==True):
       print("The function is callable")
   else:
       print("The function is non callable")
   list_1=[number_1 , number_2 , quotient , modulous]
   if(list_1.count(0)>0):
       print("There are zeroes present")
   else:
       print("No zeroes are present")
   list_1.append(4)
   list_1.append(5) 
   list_1.append(6)
   print("The new list is:",list_1)
   filtered=filter(lambda x: x>4,list_1)
   print("The filtered list:",list(filtered))
   set_1=set(list_1)
   print("The new set is:",set_1)
   set_2=frozenset(set_1)
   print("The frozen set is:",set_2)
   print("The maximum value is:",max(set_1))
   print("The hash value is:",hash(max(set_1)))
else:
    print("ERROR,Denominator cannot be 0")

print("\n********************************************************************************************************************************\n")

print("\nQuestion 4")
#Question 4
class Student():
    def __init__(self,name,rollno):
        print("Initiator called")
        self.Name=name
        self.RollNo=rollno
    def __del__ (self):
        print("The object is destroyed")
object_1=Student("Yuvraj",21104107)
print("The student name is",object_1.Name)
print("The student ROLL NO. is",object_1.RollNo)
del object_1
        
print("\n********************************************************************************************************************************\n")

print("\nQuestion 5")
#Question 5
class Employees():
    def __init__(self,name,salary):
        print("++++++++++++++++Initiator called+++++++++++++++++++++++")
        self.Name=name
        self.Salary=salary
    def __del__ (self):
        print("++++++++++++++++++The object is destroyed+++++++++++++++++++")
object_1=Employees("Mehak",40000)
print("The original salary of employee is",object_1.Salary)
object_1.Salary=70000
print("The Employee name is",object_1.Name)
print("The updated Employee salary is",object_1.Salary)
object_2=Employees("Ashok",50000)
print("The Employee name is",object_2.Name)
print("The Employee salary is",object_2.Salary)
object_3=Employees("Viren",60000)
print("The Employee name is",object_3.Name)
print("The Employee salary is",object_3.Salary)
del object_3

print("\n********************************************************************************************************************************\n")

print("\nQuestion 6")
#Question 6
#Input Word
input_word=input("Enter the word:")
test_word=input("Enter the test word:")
verify=0
for ch in input_word:
    count_input=input_word.count(ch)
    count_test=test_word.count(ch)
    if(count_input!=count_test):
        verify=1
        break
if(verify==0):
    print("You have real friendship")
else:
    print("Your friendship is fake")
    


