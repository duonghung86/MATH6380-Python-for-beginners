"""

@authors: Johnny and Thanh

"""


# This program asks for user to input Temperature in Celsius 
# and returns temperature in Farenheit.


# Asks user to input temperature in Celsius.
# Repeat until user enter properly input
loop = 0
while loop == 0:
    temp_c = input("Please enter temperature in Celsius (only number): ")    
    try:
        temp_c = float(temp_c)
        loop = 1
    except ValueError:
        loop = 0

# Returns temperature in Farenheit.
temp_f = (9 / 5) * temp_c + 32  # Convert from Celcius to Farenheit
temp_f = format(temp_f,'.1f')   # Only display 1 digit after the dot
print ('\nTemperature in Farenheit: ' + str(temp_f)+"\N{DEGREE SIGN}F")