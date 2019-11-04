# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:49:40 2019

@authors: Johnny and Thanh
"""

# Function takes in mass and velocity and returns Kinetic Energy
def kinetic_energy(mass, velocity):
    ke = .5 * mass * (velocity ** 2)
    return ke

# Main Program

# Makes sure that user has valid inputs
try:
    # Asks for mass
    mass = float(input("Please enter object's mass in kilograms: "))
    # Makes sure mass inputted is nonnegative
    assert mass > 0
    # Asks for velocity
    velo = float(input("Please enter object's velocity (in meters \
per second): "))
    # Makes sure velocity inputted is nonnegative
    assert velo >= 0
    # Calls function to calculate Kinetic Energy and prints it's return
    print('\nThe amount of kinetic energy that the object has is',kinetic_energy(mass, velo))
except ValueError:
    print('No letters allowed.')
except AssertionError:
    print('Negative numbers are not allowed.')    