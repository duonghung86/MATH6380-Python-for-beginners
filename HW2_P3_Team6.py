# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:49:40 2019

@authors: Johnny and Thanh
"""

# Function for input validation and return it after validation
def get_input(inp):
    #try to convert input to integer
    try:
        inp=float(inp)
        # verify whether the score in a proper number
        if inp < 0 :
            print('Input Error ! Please enter positive number')
            return False
        else:
            return inp
    except: 
        print('Input Error ! Please enter number only')
        return False
    
# Function to calculate BMI
def calculate_bmi(weight,height):
    bmi= weight*703/(height**2) 
    return bmi

# Function
def calculate_weight_category(bmi):
    if bmi < 18.5 :
        print(' Sorry! BMI indicates that you are underweight')
    elif bmi > 25:
        print(' Sorry! BMI indicates that you are overweight')
    else:
        print(' Congraturation! BMI indicates that you are optimal-weight')

#Main program
#Request inputs and validate them
weight = input('Please enter your weight in pounds : ')
if get_input(weight)!=False:
    wei=get_input(weight)
    height = input('Please enter your height in inches : ')
    if get_input(height)!=False:
        hei=get_input(height)
        
        #Compute the output and print the conclusion
        bmi=calculate_bmi(wei,hei)
        print('\nYour BMI is',bmi,'\n')
        calculate_weight_category(bmi)
