#Concepts in OOP:

#Practicing making an empty class:
class Empty:
  pass

class User:
  pass

#instantiating a new user from the User class:
# user1 = User()
# print(user1) #prints an empty user object with the address at <__main__.User object at 0x7f91b001bdc0>

user2 = User()
print(user2)

# E.g. Define a class called Vehicle. After the class is defined, create two instances of Vehicle.  Save one to a variable called car, and another to a variable called boat

class Vehicle:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

boat = Vehicle("Honda", "Civic", "2003")
print(boat.model)

#Instantiating a Class:
#v = Vehicle("Honda", "Civic", 2017)

#E.g.
# Define the Comment class below:
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes