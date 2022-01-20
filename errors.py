#A file to run some error-handling lines of code:

#Error Handling:

# raise ValueError('invalid value')

#Type Error:
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("Text must be an instance of a str!")
    if color not in colors:
        raise ValueError("Color is invalid color!")
    print(f"Printed {text} in {color}")

colorize(2, "red") #Prints: TypeError: Text must be an instance of a str! ValueError: Color is invalid color!

# try:
#     foobar
# except NameError as err:
#     print(err)