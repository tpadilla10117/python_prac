#Tuples:
alphabet = ("a", "b", "c", "d")
print(alphabet)
print(type(alphabet))

#for loops :
for letter in alphabet:
  print("looping through tuple: ", letter)

#while loops:
j = len(alphabet) - 1
while j >= 0:
  print( "Using while loop: ", alphabet[j] )
  j -= 1


# some_tuple = tuple(1,2,3)

#tuples can be used as keys in dictionaries:
locations = {
  (35.6895, 39.6917): "Tokyo Office"
}

print(locations)

#count method:
p = (1,2,3,4,5)
print( p.count(1) ) #tells you how much the passed in parameter occurs

#index method:
print("using the indec method on a tuple: ", p.index(1))

#Sets:

s = set({1, 4,5})
print(4 in s) #returns True

#use loop to access values:
snums = {1,2,3,4}
for number in snums:
  print("Looping through a set: ", number)

#add method:
snums.add(5)
print("After adding : ", snums) #returns {1, 2, 3, 4, 5}

#remove method:
snums.remove(5)
print("After using theremove method: ", snums) #{1, 2, 3, 4}

