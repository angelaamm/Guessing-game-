#Pyhton learning via Scrimba
'''failed_subjects =("3")
name="Daniella"
print('Dear Mrs Kalanza')
print('Your daughter' + name + ' has failed ' + failed_subjects + '  subjects.')
print(name+ ' is required to redo ' + failed_subjects + ' courses so as to proceed to the next level. ')'''
'''print(type("hello"))
print(type(538))
print(type(45.3))
print(type(True))'''
#Variables & Datatypes - Exercise
#Create appropriate Variables for Item name, the price
#and how many you have in stock
'''item_name="Chairs"
price = 3000
in_inventory =45
print(item_name,price,in_inventory)'''
#Slicing
'''msg ="Welcome to my Car yard"
#     012345678910
print(msg[4])
print(msg[-1])
print(msg[8:10])
print(msg[:7])'''

#Exercise
#From the string "Welcome to Python 101:Strings",extract text and create/print a new string that says
#*"1 Welcome Ring To Tyler"
#*Every first letter in a word should be capitalized
'''msg='Welcome to Python 101: Strings'
    #01234567891011
#msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
msg1=msg[:7]+ msg[24:28]+msg[8:10]+msg[8]+msg[12]+msg[2]+msg[6]+msg[24]
print(msg1.upper())'''
#Strings
'''msg="""Dear Mrs Sainyi,,
your son Musa has been caught climbing a an avocado tree
hence he will remain suspended for one week <3"""
print(msg)'''
#Find
'''msg ='Welcome to my Car yard'
#print(msg.find("y"))
print(msg.replace('car','cloth'))
print('Car yard'in msg)'''
'''name="Leon"
colour="blue"
print(name+ " loves the colour "+ colour)'''
#User Input
'''name=(input("What is your name? "))
age=(input("How old are you? "))
print("Hello"+name)
print("You are "+age+ "years old")'''
# name=(input("What is your name? "))
# distance_km=float(input("Distance in km"))
# distance_miles=float(distance_km)/1.609
# print(f"Hello {name.title()} {distance_km} km is equal to {round(distance_miles,1)} miles.")
'''"sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
sales_w2.append(6)
#print(sales_w2)
sales_w1.extend(sales_w2)
sales.extend(sales_w1)
print(sales)# print(sales_w1)

print(max(sales_w1))
best_day_w1=max(sales_w1)*1.5
print(f"the profit for best day w1 was ${best_day_w1}")

print(min(sales_w1))
worst_day_w1=min(sales_w1)*1.5
print(f"the profit for worst day w1 was ${worst_day_w1}")


print(max(sales_w2))
best_day_w2=max(sales_w2)*1.5
print(f"the profit for best day w2 was ${best_day_w2}")

print(min(sales_w2))
worst_day_w2=min(sales_w2)*1.5
print(f"the profit for worst day w2 was ${worst_day_w2}")

best_day =max(sales)*1.5
print(f"the profit was ${best_day}")

worst_day=min(sales)*1.5
print(f"the profit was ${worst_day}")
print(min(sales_w1))
print(max(sales))'''
#Split and join
'''msg=("Welcome  to  my  car  yard")
print(msg.split())
#print(msg.split(' '))
print(type(msg.split()))
print(''.join(msg.split()))
print(type(''.join(msg.split())))'''
#Tuple
'''friends=["Joy","Love","Peace","Patience","Hope","Paul"]
friends_tuple=("Joy","Love","Peace","Patience")
friends_set={"Joy","Love","Peace","Patience","Paul"}
my_friends_set={"Joy","Love","Peace"}
print(type(friends))
print(type(friends_tuple))
#Sets
print(type(friends_set))
print(friends_set.difference(my_friends_set))'''

#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

'''friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
#1
print('Eric' in friends and 'John' in friends)
#2.
print(friends.union(my_friends))
#3
print(friends.intersection(my_friends))
#4
print(friends.difference(my_friends))
#5
print(friends.symmetric_difference(my_friends))
#6
# cars1={'900','420','V70','911','996','V90','911','911','S','328','900'}
# print(cars1)
cars1=set(cars)
print(cars1)'''
#Functions
'''def salutations(name):
    print("Bonne nuit " +name+ "!")
salutations("Lizzie")
def greeting(name,age):
    print("Hello "+name+ " You are "+age+"!")
    print(f"Hello {name} you are {age}")
greeting("Alvin", "24")'''
'''def greetings(name,age=16):
    #print("Hello "+name+ " you are "+str(age)+ "years old")
    print(f"Hello {name} you are {age} years old")
name=(input("Enter your name:"))
greetings(name,7)
greetings("Elois")'''
#Functions Exercise
#Greets user with 'name' from 'input box' and 'age', if available, default age is used
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps
# 6. Favorite color should be in lowercase
'''def greeting(name, age=28, colour ="red"):
    #print('Hello '  +  name + ', you will be' + str(age+1) +'next birthday!')
    print(f'Hello {name.title()}, you will be {age+1} next birthday!')
    print(f"We hear you like colour {colour.lower()}!")
name = input('Enter your name: ')
age  = input('Enter your age: ')
colour=input("What is your favourite colour? ")
greeting(name,int(age),colour)'''
#Return Statements
'''def VAT(amount):
    tax=amount*0.16
    total_amount=amount*1.16
    return amount,tax,total_amount
price=VAT(64000)
print(price,type(price))'''
#Comparisons and Booleans
'''a=4
b=6
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(b>a)
print(b>=a)
print('g' in "istanangela") #membership
print('l' not in "istanangela" ) #not a member'''
#Identity
'''a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b) #because they are not the same in memory
print(id(a), id(b)) #because Ids are not identical'''
#Boolean
'''print(int(True))
print(int(False))
print(bool("Me"))
print(bool(""))
print(bool(65))
print(bool())
print(9+True+False+True+False)'''

#Conditionals: If,Elif,Else
'''raining=False
cold=False
if raining and cold:
    print("Carry an umbrella and a jacket")
elif raining and not cold:
    print("Carry an umbrella")
elif cold and not raining:
    print("Carry a jacket")
else:
    print("Sun sweater is fine")'''

#Calculator
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
'''operator = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if operator.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if operator == '+':
        print(f'Answer is: {num1 + num2}')
    elif operator == '-':
        print(f'Answer is: {num1 - num2}')
    elif operator == '*':
        print(f'Answer is: {num1 * num2}')
    elif operator == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')'''
# optimize/shorten the code in the function
# try to reduce the number of conditionals

'''def num_days(month):

    if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else: 
        print('number of days in',month,'is',30)
num_days('sep')'''

'''def num_days(month):
    days = 31
    if month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in', month, 'is', days)
num_days('feb')'''
'''def num_days(month):
    days = 31
    if month in {'apr', 'jun', 'sep', 'nov'}:
        # if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in', month, 'is', days)
num_days('jan')'''
#While LOOPS
'''i=0
while i<7:
    i=i+1
    print("Help, i am stuck in a loop.")'''
'''i=0
while i<4:
    i=i+1
    print(f"{i}." + "*" *i + "Help, im stuck in a loop." + "*" *i)'''
#Exercise
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box
#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
'''num=23
guess=0
guess_limit=5
guess_number=1
guess=int(input(f"Guess a number 1-100: "))
while guess_number<guess_limit:
    if guess !=num:
        guess_number+=1
        if guess>num:
            guess=int(input(f"{guess} too high. Guess again 1-100: "))
        else:
            guess=int(input(f"{guess} too low. Guess again 1-100: "))
    if guess==num:
        print(f"You win! you guessed it: {num}")
if guess!=num:
    print(f"You lose Guess was: {num}")'''
#For loops
'''for letter in "Holy Bible":
    print(letter)'''
'''for i in range(1,10,2):
    print(i)'''
'''for name in ['John','Terry','Eric','Michael','George']:
    print(name)'''
'''friends=['John','Terry','Eric','Michael','George']
for friend in friends:
    print(friend)'''
# friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
# for friend in friends:
#         if friend == 'Eric':
#             print('Found ' + friend + '!')
#             continue
#         print(friend)
#Nested Loops
'''friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)'''
#For loops Exercise
'''names=["KEN","tIm","Alvin","Kim"]
names1=["Graham","Terry","Jones","Musa"]
msg="You are invited to the party on Saturday."
names.extend(names1)
for index in range(2):
    names.append(input("Enter a new name: "))
for name in names:
    #msg1= f'{name.title()}! {msg}'
    msg1=name.title() + '!' +msg
    print(msg1)'''
#Enumerate this
'''Friends=["Ken","Tim","Alvin","Ian"]
i=1
for Friend in Friends:
    print(i, Friend)
    i+=1'''
'''friends=["Ken","Tim","Kim","Joe"]
for num,friend in enumerate(friends):
    print(num,friend)'''
#Sort() ,Sorted()
'''my_list=[5,1,9,4,6]
my_list1=[-4,-11,-3,7]
my_tuple=('d','h','t','b','m')
my_dict={"brand":"Porche","year":"2024","model":"Cayenne"}
string="Hamilton"
print(my_list,'original')
#print(my_list.sort())
print(sorted(my_list),'new')
print(my_dict,'original')
#print(sorted(my_dict.items()))
print(sorted(my_dict.values(),reverse=True))
print(my_dict,'new')
print(sorted(my_list1))
print(sorted(my_list1, key = abs))'''
#Dictionaries = used to store key value pairs
movie={
    "title":"The Devil Wears Prada",
    "year":"2006",
    "cast":"Anne Hathaway"}
#movie["title"]="Interstellar"
#movie["no_of_cast"]=68
'''movie.update({"title":"Interstellar","year":"2014","cast":"Anne Hathaway","no_of_cast":68})
#del movie['cast']
#year=movie.pop("year")
print(movie)
#print(year)
print(movie.keys())
print(movie.values())
for key, value in movie.items():
    print(key,value)'''
'''people={"Claudia":52,"Patrice":21,"Melody":14,"Elon":59}
if 'Aaron' not in people:
    print("He\'s not here")
creatures={"Lion":22,"Elephant":78,"Tigre":44,"Rhino":37}'''
#Method 1 update
'''living_things={}
living_things.update(people)
living_things.update(creatures)
print(living_things)
#Method 2 comprehension
for groups in (people,creatures):living_things.update(groups)
print(living_things)'''
#Method 3 unpacking
'''living_things={**people,**creatures}
print(sorted(living_things.items()))
print("The sum of ages is: ",sum(people.values()))'''
#Exercise Dictionaries
'''freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

#create an dempty shopping cart
cart = {}
#loop through stores/dicts
for shop in (freelancers,antiques,pet_shop) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
print(f'You Purchased {list(cart.keys())} Today it is all free. Have a nice day of mayhem!')'''
#File handling
#To Create a new file
'''with open("Houses.txt","w") as file:
    print(file.write())
#To write contents in the file
with open("Houses.txt","a") as file:
    file.write("\n11 bedroom with 15 and half baths\n"
    "3 bedroom with 2 baths\n"
    "7 bedroom with 6 baths\n")
#To read the file
with open("Houses.txt","r") as file:
    print(file.read())'''
# Execptions try/except,raise
