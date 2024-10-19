import time
from tarfile import TruncatedHeaderError

#Variables is a container for a value
'''Weight = 48
height=180
grade='a'
name="angie"
#Float
price=100.00
price_total =123456.2452
print(type(price_total))'''
import math

'''
#string
first_name ="Ndengu"
last_name ="Omera whats up"
full_name=first_name + last_name
print("Chapo nne na"+str(full_name))'''
#integer
'''weight = 49
weight +=1
print("My weight is: "+str(weight)+"Kg")'''
#Boolean
'''Robot =False
print("Are you a human?"+str (Robot))
print(type(Robot))'''

#Multiple assignment=assigning multiple variables at the same time in one line of code
'''Brand,Cream,Size,Price="Nivea","Perfect and radiant",50,900
print(Brand)
print(Cream)
print(str(Size)+"ml")
print(str(Price)+"Ksh")'''
#string method
'''name="Kris baby"
print(name.__len__())
print(name.find('b'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('b'))'''
#type cast = converting data type of a value to another data type
'''a=2
b=4.7
c="6"
print(a)
print(b)
print(c*6) #to show its a string
#now to type cast
a=str(a)
b=int(b)
c=float(c)
print(a)
print(b)
print(c)'''
#User input
'''Name =input("What is your name?: ")
Grade= input("What grade are you in?: ")
AP = input("Which AP class do you take?: ")
print(Name)
print(Grade)
print(AP)'''
'''Name=input("What is your name?: ")
Grade=int(input("Which grade are you in?: "))
AP=input("Which AP class do you take?: ")
print("Hello"+str(Name))
print("You are in grade"+str(Grade))
print("Your major is"+str(AP))'''
#Math Functions
'''a=7.6
b=4
c=87
print(round(a))
print(math.ceil(a))
print(math.floor(a))
print(abs(a))
print(pow(a,2))
sqrt=math.sqrt(a)
print(round(sqrt,2))
print(max(a,b,c))
print(min(a,b,c))'''
#If statements = A block of code executes if a condition is true.
'''Grade =int (input("What grade are you in? "))
if Grade >=6:
    print("You are a senior")
elif Grade <1:
    print("You are still in Kindergarten")
else:
    print("You are a junior")'''

#Logical operators = Used to check if two or more conditions are true.
'''grade =str(input("What grade did you get?")).lower()
print(grade)
if grade=="e"or grade=="d":
    print("Fail")'''
#temp =int(input("What is the temp today? "))
#if (temp >=0 and temp <=30):
  #  print("The temp is good outside")
#if (temp <0 or temp >30):
#     print ("The weather is harsh outside")
#print largest number
'''a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if(a>b and a>c):
    print("a is the largest")
elif (b>a and b>c):
    print("b is the largest")
else:
    print("c is the largest")'''
'''marks =int(input("What mark did you get? "))
if not (marks >=80 and marks <=100):
    print("A")
elif (marks >=70 and marks <=80):
    print("B")
elif(marks>=60 and marks <=70):
    print("C")
else:
    print("D")'''
#While Loop
'''n = 1
while n < 10:
    print(n)
    if n==6:
        #break
        continue
    n+=1'''

#Simple calculator
'''num1=float(input("Enter first number "))
operator =(input("Enter an operator + - * /: "))
num2=float(input("Enter second number "))
if operator =="+":
    result=num1+num2
print(result)
elif operator== "-":
    result=num1-num2
print(result)
elif operator=="*":
    result=num1*num2
print(result)
elif operator =="/":
    result=num1/num2
print(result)
else:
    print("unknown operation")'''
#For loop = a system that will execute its code a limited number of times
# for loop
'''for i in range(10):
    print(1)'''
#for i in range (10,20):
 #   print(i)
'''for i in range(10,20,2):
     print(i)'''
'''for i in  "Angela":
    print(i)'''
'''for countdown in range (10,0,-1):
    print(countdown)
    time.sleep(1)
print("Youre the best")'''
#Nested loops
'''rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()'''
''''numbers = [1,2,3,4,5,6]
#sum_=0
for num in numbers:
    num_sq=num*num
    #sum_=sum_+num_sq
print("The sum of numbers is: ",num_sq)'''
#Loop control statements = change a loop execution form its normal sequence
#break #continue #pass
#break
'''while True:
    name=(input("Enter your name"))
    if name!= "":
      break'''
#continue
'''phone_number = "0717-783-045"
for i in phone_number:
    if i =="-":
     continue
    print(i,end="")
    #print(i)'''
#pass
'''for i in range(1, 20):

    if i == 15:
        pass
    else:
        print(i)'''
#List = used to store multiple items in a single variable
'''Device =["Vitron","Sony","LG","Hisense"]
#print(list[3])
for x in Device:
    if x=="Sony":
        continue
    else:
        print(x)'''
'''Device=["Vitron","Sony","LG","Hisense"]
Device[2]="TCL"
print(Device[2])'''

#2D Lists
'''Pens=["Bic","Pilot","Kasuku"]
Pencil=["Staedler","Pelican","Nataraj"]
Ruler=["Hacco","Nataraj","Gelx"]
Stationery=(Pens,Pencil,Ruler)*2
print(Stationery)'''
#[1][0])
#Tuples =collection which is ordered and unchangeable used to group together related data
'''student=("Mwalimu",24,"female")
print(student.count("Mwalimu"))
print(student.index("Mwalimu"))
print(student)
for x in student:
    print(x)
    if "Mwalimu":
        pass
    print(x)'''
#Set =a collection which is unordered and unindexed. No duplicate values
'''Books={"Exe book","Text books","Encylcopedia"}
Pens ={"Pencils","Pens","crayons"}
#Books.remove("Encylcopedia")
#Pens.update(Books)
Stationary=Books.union(Pens)
for x in Stationary:
    print(x)'''
#Dictionary = Unordered collection that helps store keys value pairs
'''capitals={"Kenya":"Nairobi",
         "Uganda":"Kampala",
          "Tanzania":"Dodoma"}
#print(capitals["Tanzania"])
#print(capitals.get("Rwanda"))
print(capitals.values())
print(capitals.items())
capitals.pop("Uganda")
capitals.clear()
for key,value in capitals.items():
    print(key,value)'''
#Index = gives access to a sequence of elements
'''name ="angela mumbi"
second_name=name[6:].upper()
print(second_name)'''
#Functions = block of code that is only executed when it is called.
'''def hello(first_name,last_name,age):
    print(f"Hello {first_name} {last_name}")
    print(f"You are {age} years old.")
    print("Have a nice day.")
hello('Zoey','Johnson',21)'''

#Dict
Johnson={"Zoey":"3rd year",
        "Andre jr":"F4",
        "Diane":"G7",
        "Jack":"G7",
        "Devante":"PP2"}
#print(Johnson)
#print(help(Johnson))
'''print(Johnson.get("Zoey")) 
if Johnson.get("Zaara"):
    print("Is a Johnson")
else:
    print("Is not a Johnson")'''
'''Johnson.update({"Annika":"G2"}) #add annika to list
Johnson.update({"Zoey":"Corporate baddie"}) #change value in Zoey
Johnson.pop("Devante")'''
#Johnson.popitem()
#Johnson.clear()
#Johnson.keys()
'''items=Johnson.items()
print(items)
print(Johnson)'''
'''for keys in Johnson.keys():
    print(keys)
for values in Johnson.values():
    print(values)'''
for key,value in Johnson.items():
    print(f"{key} ,{value}")