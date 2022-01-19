#Functions:
def say_hi():
  print("Hi!")
  
# say_hi() #prints Hi!

def make_noise():
    print("THE CROWD GOES WILD")
#Then, call make_noise once:
# make_noise()

def print_square_of_7():
  print(7**2)

# print_square_of_7()

#function with return keyword:
def square_of_7():
  return 7**2
result = square_of_7()

print(result) #prints 49

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    return [x for x in range(1,50) if x % 2 == 0]

# print(generate_evens() )

#Altering functions to accepts parameters:
def square(num):
  return num*2
print( square(8) ) #prints 16

#Parameters and f strin interpolation:
def print_full_name(first_name, last_name):
  return (f"Your full name is {first_name} {last_name}")

print(print_full_name("Trin", "Padilla") )

#Practice: sum_odd_numbers:
def sum_odd_numbers(numbers):
  total = 0
  for num in numbers:
    if num % 2 != 0:
      total += num
  return total

print( "Invoking sum_odd_numbers: ", sum_odd_numbers([1,2,3,4,5]) )

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

#Assigning a default value:
def exponent(num,power=2):
  return num **power

print("Running the exponent function: ",exponent(2))


days = {"1":"Sunday", "2":"Monday", "3":"Tuesday", "4":"Wednesday", "5":"Thursday", "6":"Friday", "7":"Saturday"}
print(days.get("2"))

sample_days=["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]

print(sample_days[2])

def return_day(num=1):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

print(return_day(1))

#Write a function called last_element.  This function takes in one parameter (a list) and returns the last value in the list.  It should return None if the list is empty:

#takes in a list
def last_element(param):
    #param[-1] gives the last item in the list
    if param:
        return param[-1]
    return None
  
#Function takes in 2 parameters (both numbers).  If the first is greater than the second, this function returns "First is greater" if the second number is greater than the first, returns "Second is greater"
def number_compare(num1, num2):
    if num2 < num1:
        return "First is greater"
    elif num2 > num1:
        return "Second is greater"
    return "Numbers are equal"


def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

#Write a function that accepts a list and a search term (this will always be a primitive value) and returns the number of times the seearch_term appears in the list:

def frequency(collection, term):
    return collection.count(term)

#Write a function that accepts a list of numbers and returns the product of all even numbers in the list:

def multiply_even_numbers(collection):
    product = 1
    for num in collection:
        if num % 2 == 0:
            product = product * num
    return product

#Keyword Arguments with Functions:
def full_name(first, last):
  return "Your name is {first} {last}"

print(full_name(first="Trin", last="Padilla") )

#Global Scoping:
total = 0
def increment():
  global total
  total += 1
  return total

print("Invoking increment and practiving using the global scope: ", increment() ) # prints 

#nonlocal scoping:
def outer():
  count = 0
  def inner():
    nonlocal count
    count += 1
    return count
  return inner()

print( "Practicing using the nonlocal scope: ", outer() ) #prints 1

#Practicing Documenting Functions:
def say_hello():
  """A simple function that returns the string hello """
  return "Hello!"

print( say_hello.__doc__) #A simple function that returns the string hello 

#Using *args :
def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  return total

print("Practicing using the *args operatot: ", sum_all_nums(4,6,9,4, 10) ) #prints 33


def ensure_correct_info(*args):
  if "Colt" in args and "Steele" in args:
    return "Welcome back Colt!"
  return "Not sure who you are..."

print( ensure_correct_info(1, True, "Steele", "Colt") )
print( ensure_correct_info())