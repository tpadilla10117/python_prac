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