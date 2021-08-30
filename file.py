num1 = 42 # - variable declaration
num2 = 2.3 # - variable declaration
boolean = True 
"""
- Data Types
    - Primitive
        - Boolean 
 """
string = 'Hello World' # Data Type -Premitive -String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Array of Strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1]) #print Sausage
pizza_toppings.append('Mushrooms')
print(person['name']) #print John
person['name'] = 'George' #  change value 'name' from 'John' to 'George'
person['eye_color'] = 'blue' #adding value to Person Array 
print(fruit[2]) #print banana

if num1 > 45:  #conditional statement
    print("It's greater") 
else: #conditional statement
    print("It's lower") #this will print because 42 < 45

if len(string) < 5: #conditional statement
    print("It's a short word!")
elif len(string) > 15: #conditional statement
    print("It's a long word!")
else: #conditional statement
    print("Just right!") #this will print

for x in range(5): # for loop i=0, i>5, +1)
    print(x) # print 1-4
for x in range(2,5): #for loop (i=2, i>5, +1)
    print(x)  # print 2-4
for x in range(2,10,3): # for loop (i=2, i>10, +3)
    print(x)
x = 0 # change value of x to 0
while(x < 5): # while loop start at 0 stop at 4
    print(x)  # prits current value of x
    x += 1    # incrament x value by 1

pizza_toppings.pop()  # no print to show change
pizza_toppings.pop(1) # no print to show change

print(person) # Print person Array
person.pop('eye_color') # removes 'eye_color': 'blue' 
print(person) # Print person Array without eye_color vlaue

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # not used/not printed
    for num in range(10):
        print('Hello')

print_hello_ten_times() # no Print print is part of name not a command

def print_hello_x_times(x): # not used/not printed
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # no Print print is part of name not a command

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #will print
print_hello_x_or_ten_times(4) #will print


"""
Bonus section
"""

# print(num3) ##- NameError: name <variable name> is not defined
# num3 = 72 - add var and its value
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team' no team named
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) #- IndentationError: unexpected indent
# fruit.append('raspberry') #- AttributeError: 'tuple' object has no attribute 'append
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'