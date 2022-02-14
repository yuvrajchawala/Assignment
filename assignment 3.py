print("Question 1\n")
#Question 1
#To input string
input_string=input("Enter your string: ")
#To check input is a sentence or word and solving for word
if(input_string.count(" ")==0):
    for ch in input_string:
        print("THE OCCURANCE OF" ,ch ,"is:",input_string.count(ch))
#For String to be sentence
else:
    input_string=input_string+" "
    r=""
    for ch in input_string:
        r=r+ch
        if(ch!=" "):
            continue
        print("The occurance of",r,"is:",input_string.count(r))
        r=""

print("\n***********************************************************************************************************\n")        
              
print("Question 2\n")
#Question 2
#To input the date
input_day=int(input("ENTER THE DAY [1-31]:"))
input_month=int(input("ENTER THE MONTH[1-12]:"))
input_year=int(input("ENTER THE YEAR[1800-2025]:"))
def checking():
    if(1<input_day<31 and 1<input_month<12 and 1800<input_year<2025):
        return True
    else:
        return False
check=checking()
if(check):
 if(input_year%4==0):
    leap_year=True
 else:
    leap_year=False
 if input_month in (1,3,5,7,8,10,12):
    month_length=31
 elif(input_month==2):
    if(leap_year):
        month_length=29
    else:
        month_length=28
 else:
    month_length=30

 if(input_day<month_length):
    input_day=input_day+1
 else:
    if(input_month==12):
        input_month=1
        input_year=input_year+1
    else:
        input_month=input_month+1
        input_day=1
 print("THE NEXT DATE IS",input_day,input_month,input_year)
else:
    print("PLEASE ENTER THE DATE ACCORDING TO INSTRUCTIONS")
    
print("\n***********************************************************************************************************\n")

print("Question 3\n")
#Question 3
#To input the number of enteries user want to enter
NO_Entries=int(input("ENTER NO. OF ENTERIES YOU WANT TO ENTER:"))
output_list=[]
input_list=[]
#To input the entries
for i in range(0,NO_Entries):
    Entries=int(input("Enter the entry:"))
    #To create tupple and input list
    TUPPLE=(Entries,Entries*Entries)
    input_list.append(Entries)
    output_list.append(TUPPLE)
    #To print the lists
print("Input list is:",input_list)
print("Output list is:",output_list)

print("\n***********************************************************************************************************\n")

print("Question 4\n")
#Question 4
#To input the grade by user
input_grade=int(input("Enter grade of student between 4 and 10:"))
#To check the grade
if(input_grade==4):
    print("Your Grade is 'D' and Poor Performance")
elif(input_grade==5):
    print("Your Grade is 'C' and Below Average Performance")
elif(input_grade==6):
     print("Your Grade is 'C+' and Average Performance")
elif(input_grade==7):
     print("Your Grade is 'B' and GOOD Performance")
elif(input_grade==8):
     print("Your Grade is 'B+' and Very Good Performance")
elif(input_grade==9):
     print("Your Grade is 'A' and EXCELLENT Performance")
elif(input_grade==10):
     print("Your Grade is 'A+' and OUTSTANDING Performance")
else:
    print("ERROR!\n"'Enter in given range')
          
print("\n***********************************************************************************************************\n")

print("Question 5\n")
#QUESTION 5
chr_length=76
for columns in range(0,6):
    spaces=0
    for spaces in range(0,columns):
        print(" ",end='')
    for rows in range(65,chr_length):
        print(chr(rows),end='')
    chr_length=chr_length-2    
    print()

print("\n***********************************************************************************************************\n")

print("Question 6\n")
#Question 6'
#To ask user if he wants to run the program
z=input("Enter 'Y' if you want to give entry and 'N' to finish program:")
dict1={}
while(z=="Y"):
    SID=int(input("ENTER SID:"))
    NAMES=input("Enter name of student:")
    dict1.update({SID:NAMES})
    z=input("Enter 'Y' if you want to give another entry and 'N' to finish program:")
    if(z=='N'):
        break
if(z=="N"):
    print("The final dictionary is:",dict1)
print("The sorted dictionary by 'NAMES' is:",sorted(dict1.items(),key= lambda x:x[1]))
print("The sorted dictionary by 'SID' is:",sorted(dict1.items()))
input_search=int(input("Enter SID you want to search:"))
if(input_search in dict1):
    print("The student name is:",dict1[input_search])
else:
    print("SID not present")

print("\n***********************************************************************************************************\n")

print("Question 7\n")
#Question 7
First_element=0
Second_element=1
Total_elements=int(input("Enter the no. of entries:"))
if(Total_elements<=0):
    print("Enter a natural number")
elif(Total_elements==1):
    print(First_element)
    print("AVERAGE=1")
else:
    Fibonacci=[0,1]
    for i in range(0,Total_elements-2):
        Next_element=First_element+Second_element
        Fibonacci.append(Next_element)
        SUM=1+Next_element
        First_element=Second_element
        Second_element=Next_element
    print("The Fibonacci series is:",Fibonacci)    
    print("AVERAGE=",SUM/Total_elements)

print("\n***********************************************************************************************************\n")

print("Question 8\n")    
#Question 8
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
set4 = set1^set2
print("The answer of 8.a:",set4)
set5 = set1^set2^set3
print("The answer of 8.b:",set5)
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print("The answer of 8.c:",set6)
set7 = set(range(1,11)) - (set1)
print("The answer of 8.d:",set7)
set8 = set(range(1,11)) - (set1|set2|set3)
print("The answer of 8.e:",set8)
   

    
     
