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