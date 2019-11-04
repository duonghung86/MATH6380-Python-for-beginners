# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:58:46 2019

@authors: Johnny and Thanh
"""

def validate_input(score):
    #try to convert score to integer
    try:
        score=int(score)
        # verify whether the score in a proper number
        if score < 0 or score > 100 :
            print('Input Error ! Please enter number between 0 and 100')
            return False
        else:
            return True
    except: 
        print('Input Error ! Please enter number only')
        return False
    
def calculate_grade(score):
    
    grade_letters='FDCBA' # Grade letters
    grade_scores=[0,60,70,80,90,101]  
    i=0
    # Identify score belongs in which range
    while i<6:
        if score>=grade_scores[i] and score<grade_scores[i+1]:
            grade=grade_letters[i]
            break
        else:
            i=i+1
    return grade

#Main program
#Display Information
print('Score   Grade')
print(' >=90     A   ')
print(' >=80     B   ')
print(' >=70     C   ')
print(' >=60     D   ')
print('  <60     F   ')
score=input('Please enter the course grade: ')

if validate_input(score):
    score=int(score)
    print('=>',calculate_grade(score), ' Grade')
