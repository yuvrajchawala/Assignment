print('Question 1\n')
#Question 1
b='Python is a case sensitive language'#input string
#To find length
c=len(b)
print("The length of given string is:",c)
#To reverse the string
Reverse=b[::-1]
print("Reversed string is:",Reverse)
#To store in a new string
e=b[9:26]
print("New stored string is:",e)        
#To replace the given substring
f=b.replace('a case sensitive','object oriented')
print("New string is:",f)
#To find the index of 'a'
print("The index of a is:",b.find('a'))
#To remove white spaces
print(b.replace(' ',''))

print('***********************************************************************************\n')

print("Qustion 2\n")
#Question 2
#To store your 'SID','NAME','CGPA','DEPARTMENT NAME(DN)'
SID=21104107
NAME='YUVRAJ CHAWALA'
CGPA=9.9
DN='ELECTRICAL'
#To print the given output
print("Hey",NAME,",Here!")
print("My SID is",SID)
print("I am from",DN,"department and my CGPA is",CGPA)

print('***********************************************************************************\n')

print("Qustion 3\n")
#Question 3
#To enter the numbers
a=56
b=10
#To print the given code
print("a&b:",a&b)
print("a|b:",a|b)
print("a^b:",a^b)
print("a left shifted by 2 bits is:",a<<2)
print("b left shifted by 2 bits is:",b<<2)
print("a right shifted by 2 bits is:",a>>2)
print("b right shifted by 4 bits is:",b>>4)

print('***********************************************************************************\n')

print("Qustion 4\n")
#Question 4
#To input 3 numbers from user
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))       
#To check larger among first 2 numbers
larger=max(a,b)
#Now to check larger among larger and third number and print it
print("The largest number is:",max(larger,c))

print('***********************************************************************************\n')

print("Qustion 5\n")
#Question 5
#To input a string
String=input("Enter your string:")
#To check the presence of word 'name'
d="name" in String
if(d==True):
    print("YES,'name' is present")
else:
    print("NO,'name' is absent")

print('***********************************************************************************\n')

print("Qustion 6\n")    
#Question 6
#To input three sides of a triangle
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
#To check the formation of triangle
if(((a+b)<c)|((a+c)<b)|((c+b)<a)):
    print("Triangle is not possible")
else:
    print("Triangle is possible")


































