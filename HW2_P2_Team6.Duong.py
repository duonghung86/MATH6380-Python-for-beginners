# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:49:23 2019

@authors: Johnny and Thanh
"""
# Function for input validation
def validate_input(inp):
    #try to convert input to integer
    try:
        inp=int(inp)
        # verify whether the input in a proper number
        if inp < 0 :
            print('Input Error ! Please enter positive number')
            return False
        else:
            return True
    except: 
        print('Input Error ! Please enter number only')
        return False
    
# Function to calculate the kinetic energy
def calculate_ke(mass,velo):
    kinetic_energy= 0.5*mass*velo**2 
    return kinetic_energy

#Main program
mass = input('Please enter the mass in kilograms: ')
if validate_input(mass):
    velo = input('Please enter the velocity in meters per second: ')
    if validate_input(velo):
        kin_ene=calculate_ke(float(mass),float(velo))
        print('\nThe amount of kinetic energy that the object has is',kin_ene)
