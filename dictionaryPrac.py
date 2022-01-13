# Dictionaries:
  #Broken into key-value pairs like JS object
#E.g. :
instructor = {
  "name": "Trin",
  "plays_guitar": True,
  "codes_things": True,
  "last": "Padilla"
}

print(instructor["name"])

sample_dictionary = dict(games = 'uncharted')

print(sample_dictionary) #prints dictionary
print(f"{instructor['name']} {instructor['codes_things']}")

  #looping through dictionaries:
for value in instructor.values():
  print(value) #prints the values
  
  #looping through dictionaries:
for value in instructor.values():
  print(value) #prints the values

for value in instructor.keys():
  print(value)

for key, value in instructor.items():
  print(key, value)

for value in instructor.items():
  print(value)
  # ('name', 'Trin')
  # ('plays_guitar', True)
  # ('codes_things', True)
  # ('last', 'Padilla')


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0

for value in donations.values():
    total_donations += value
    print(total_donations)

print("name" in instructor) #prints True
print("phone" in instructor) #prints false
print("name" in instructor.keys() ) #prints true

# .clear() method:
fake_dictionary = dict(a=1, b=2)
print(fake_dictionary)
print(fake_dictionary.clear()) #None

  # .copy() method:
c = instructor.copy()
print(c) #prints the copied instructor dictionary

  # .fromKeys() method:
a = {}.fromkeys("a","b")
b = {}.fromkeys(["email"], 'unknown')
d = {}.fromkeys("a", [1,2,3])
print(a)
print(b)
print(d)

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

initial_game_state = dict.fromkeys(game_properties, 0)

print(initial_game_state)

  # .get() method:
print(instructor.get("name")) #prints Trin

#.pop() method:
games_owned = {
  "playstation" : "uncharted",
  "switch": "zelda",
  "xbox" : "halo"
}
print(games_owned.pop("switch")) #prints zelda

  #.popitem() method:
print(games_owned.popitem()) #returns a random key-value pair

  #.update() method:
first = dict(a=1, b=2, c=3)
second = {}
second.update(first)
print(second) #second now has the contents of first

#overwrite existing key:
second['a'] = "AMAZING"
print("Here is updated second: ", second)

#Practice -
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}


#Dictionary Comprehension:
prac_nums = dict(first=1, second=2, third=3)

squared_nums = {key: value ** 2 for key, value in prac_nums.items() }

print("After running the dict comprehension: ",squared_nums)
#After running the dict comprehension:  {'first': 1, 'second': 4, 'third': 9}

str1 = "ABC"
str2 = "123"

combo = {str1[i]: str2[i] for i in range(0, len(str1) ) }

print("Here is the combo variable: ", combo) #Here is the combo variable:  {'A': '1', 'B': '2', 'C': '3'}

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer ={}

answer = {list1[i]:list2[i] for i in range(0, 3)}

print("The answer: ", answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

person_answer = {x[0]:x[1] for x in person}

print("Here is person_answer: ", person_answer)

# person_answer = dict(person)

# print(person_answer)

asc2 = {i: chr(i) for i in range(65,91)}
print(asc2)
