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