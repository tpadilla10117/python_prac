#assignment of multiple variables:

people, friends = 10, 5
print(people)
print(friends)
words = "I am some words"
print( type (people) )
print (type (words ) )

#booleans have to be uppercase e.g. True
print(type(True) )

#Example of a list (which is like arrays):
shop = [1, 2]
print (type (shop))

#Example of a dictionary (like objects in JS):
people = {"first_name": "Trin", "last_name": "Padilla"}
print(people)
print (type (people))

#the None type:
print (type(None))

#Escape characters:
  #/n prints a new line
new_line = "hi \nthere"
print(new_line)

#String Concatenation:
str_one = "hi"
str_two = "there"
print(str_one + str_two)

# += can be used to reassign
str_one += " fran"
print(str_one)

#String Interpolation:
  #F Strings
x = 10
formatted = f"I've told you {x} times!"
print(formatted)

  #format() method
fruit = "banana"
ripeness = "ripe"
print("The {} is {}".format(fruit, ripeness) )

#Strings have indices:
print(fruit[0]) #outputs: b
print(ripeness[2]) #outputs: 
print(fruit[-1]) #outputs: "a"

#Data type Conversion:
num = 12
print(type(num))
num = float(num)
print(type(num)) #output: converted to class 'float'
print(num) #output: 12.0
print(str(8))

#Booleans:
  #input() function:
person = input("Who is this person?")
print("You said " + person)

  #if-else statements:
if person == "Arya Stark":
  print("Valar Morghulis")
elif person == "Jon Snow":
  print("You know nothing")
else:
  print("Carry on")

  #Truthiness:
    # 0 has inherit falsyness, while 1 is true
  if 1:
    print("Yay!")

  #Logical Operators"
  #and logic -
age = 6
# print(age > 2 and age < 8) #prints true
if age > 2 and age < 8:
  print("You pay child price") #prints the string

  #or logic:
city = input("Where do you live?")
if city == "LA" or city == "SF":
  print("You live in CA")
elif city == "Portland":
  print("Dream of the 90s is alive")
else:
  print("Not CA")

#Loops:
  #for loops:

  #for item in iterable_object:
    # do something
  # word = "hello"
  # for char in word:
  #   print(char)

  # arr = [40, 41, 42]
  # for num in arr:
  #   print(num) #40 41 42 (after each iteration)

  #printing ranges for for loops:
  # for number in range(1, 8):
  #   print(number)
    #prints -> 1, 2, 3, 4, 5, 6, 7

  #more ranges:
  # r = range(10)
  # print(list(r)) #gives a list [0,1,2,3,4,5,6,7,8,9,]

  # r2 = range(1, 10, 2)
  # print(list(r2)) #gives [1, 3, 5, 7, 9]

  # for num in range(10,20,2):
  #   print(num)
  #   #prints 10 12 14 16 18

  # r3 = range(8,0,-2)
  # print(list(r3) ) #[8, 6, 4, 2]

  # times = input("How many times do I have to tell you? ")
  # times = int(times)

  # for time in range(times):
  #   print(f"Number of times: {time + 1}: Clean up your room!")
  #   #prints statement based on the number a user inputs

  # for nums in range(1, 21):
  #   if nums == 4 or nums == 13:
  #     print(f"{nums} is the iterable: x is unlucky")

  #   if nums % 2 == 0:
  #     print(f"{nums} is the iterable: x is even")

  #   if nums % 2 == 1:
  #     print(f"{nums} is the iterable: x is odd")

  ## while Loops:
    # while im_tired:
    #   #seek caffeine
  # msg = input("What's the secret password?")
  # while msg != "bananas":
  #   print("incorrect")
  #   msg =input("What's the secret password?")
  #   print("Correct")

  # digits = 1
  # while digits < 11:
  #   print(digits)
  #   digits += 1 #prints numbers 1 - 10

  #break keyword:
  for x in range(1, 101):
    print(f"{x} iterable: {x}")
    if x == 15:
      break

#Lists:
  #E.g. tasks = ["Install Python", "Learn Python", "Take a break"]
  tasks = ["Install Python", "Learn Python", "Take a break"]
  print(len(tasks) ) #prints 3
  print(tasks[0]) #accesses first list item
  print(tasks[-1])
  print("Install Python" in tasks) #prints True
  tasks[2] = "Leetcode" #reassign index
  print(tasks)

  #Using list() to make a list:
  r = range(1, 10)
  print(list(r))

  #Iterating through Lists with for loops:
  # for things in tasks:
  #   print(things)

  # numerals = [4, 6, 2, 9, 7, 10]
  # for num in numerals:
  #   print(num * num)

  #Iterating though lists with While Loops:
  numerals = [1, 2, 3, 4]
  # i = 0
  # while i < len(numerals):
  #   print(f"Index {i}: {numerals[i]}")
  #   i += 1

    # .append() :
  numerals.append(5)
  print(numerals)
  
    # .extend() :
  numerals.extend([6, 7, 8, 9 , 10])
  print(numerals) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # insert() :
  numerals.insert(11, 11)
  print(numerals)

    # clear() :
  # numerals.clear()
  # print(numerals) #prints []

    #.pop() :
  # print(numerals.pop() ) #prints 11
  # print(numerals.pop(0) )

    # .remove() :
  # numerals.remove(4)
  # print(numerals) #removes 4 from the list

    #.index() :
  # print(numerals.index(1) )

    #.count() :
  # print(numerals.count(1)) #1 occurs 1 time

    #.reverse() :
    #reverse a list in place
  # numerals.reverse()
  # print(numerals)

  #.sort() :
  # numerals.sort()

  #slicing:
    #some_list[start:end:step]
  first_list = [1, 2, 3, 4]
  print(first_list[3:] ) #prints 4
  print(first_list[-1:] ) #prints 4
  print(first_list[:2]) #prints [1,2]

  second_list = ['red','green','yellow','blue', "brown"]
  print(second_list[1:]) #prints ['green', 'yellow', 'blue']
  print(second_list[0:2]) #prints ['red', 'green']
  print(second_list[0::2]) #prints ['red', 'yellow', 'brown']

  string1 = "This is fun"
  print(string1[::-1]) #reverses a string
  
  #modify portions of list with slice:
  # nums = [1,2,3,4,5]
  # nums[1:3] = ['a','b','c']
  # print(nums) #[1, 'a', 'b', 'c', 4, 5]
  # print(nums[-2])

  #swapping values:
  # names = ["James", "Michelle"]
  # names[0], names[1] = names[1], names[0]
  # print(names)

  #Begining with List Comprehensions:
  # nums = [1,2,3]
  # print([x * 10 for x in nums] )
  #[10,20,30]

  nums = [1,2,3,4,5]
  doubled_numbers = [number * 2 for number in nums]
  print(doubled_numbers)
  #[2, 4, 6, 8, 10]

  string_list = [str(num)for num in nums]
  print(string_list)
  #['1', '2', '3', '4', '5']

    #Can use Conditional logic with list comprehensions:
  evens = [num for num in nums if num % 2 == 0]
  print(evens) #[2,4]

  print( [num*2 if num % 2 == 0 else num/2 for num in nums] ) #[0.5, 4, 1.5, 8, 2.5]

  name = 'Trin'
  print([char.upper() for char in name] )
  #['T', 'R', 'I', 'N']

 #Nested Lists:
  nested_list = [ [1,2,3], [4,5,6], [7,8,9] ]

  print(nested_list[0][1]) #prints 2
  print(nested_list[1][-1]) #6

  #first loop goes through top level
  for l in nested_list:
    #gives us access to the values in the second level:
    for val in l:
      print(val) #1 2 3 4 5 6 7 8 9
      
  answer = [ [var for var in range(0,3)]]
  print("Result of first call:", answer)

  answer = [ [var for var in range(0,3)] for var in range(0,3)]
  print("The nested call:", answer)