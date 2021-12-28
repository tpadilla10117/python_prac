print("How many kilometers did you cycle today?")
kms = input() #waits for user to enter something and hitt the return key
    #Originally a string

miles = float(kms)/1.60934
miles = round(miles, 2)
#round() function takes a 1) thing to round, 2) how many decimal points to round to:

print(f"Your {kms} is equal to {miles} miles ") 