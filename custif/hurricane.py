#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'What is the current wind speed? '

# wrap windSpeed in a float() to accept decimals as numbers
windSpeed = float(input("What is the current wind speed?"))

# if input value was higher or equal to 25
if windSpeed <= 40:
    print(windSpeed)
    message =  'you are in a tropical storm.'
elif (windSpeed <= 74) :
    print(windSpeed)
    message =  'you are in a Cat 1 hurricane.'
elif (windSpeed <= 110) :
    print(windSpeed)
    message =  'you are in a Cat 2 hurricane.'
elif (windSpeed <= 129) :
    print(windSpeed)
    message =  'you are in a Cat 3 hurricane.'
elif (windSpeed <= 155) :
    print(windSpeed)
    message =  'you are in a Cat 4 hurricane.'
elif (windSpeed >= 156) :
    print(windSpeed)
    message =  'you are in a Cat 5 hurricane.'
    
print(message)