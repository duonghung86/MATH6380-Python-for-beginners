# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:16:47 2019

@author: Duong Hung
"""
''' ASCII A=65,Z=90 a=97,z=122, space=32'''
import time as tm
# Check whether a string without space character is a proper word
def validate_word(inp):
    hav_nor_cha=False # Does the string contain normal character
    for i in range(len(inp)):
        asc_val=ord(inp[i]) # convert to ASC value
        # a normal character has ASC value in range [65;90] or [97;122]
        validation=(asc_val>=65)*(asc_val<=90)+(asc_val>=97)*(asc_val<122)
        hav_nor_cha += validation
    return hav_nor_cha

# Word counter function
def word_counter(inp):
    spl_str=inp.split() # Split string by space
    counter=len(spl_str) 
    # Verify wheter each splitted string contain a normal character
    # If a splitted string does not contain any normal character, it is removed
    for i in range(len(spl_str)):
        if validate_word(spl_str[i]) == False:
            counter -= 1
    return counter

# Calculate the average number of letters
def ave_nol(inp):
    anol = len(inp)/word_counter(inp)
    anol = round(anol,2)
    return anol

# Count the upper or lowercase character
    #if uppercase ul=1, else ul=0
def count_ul_cha(inp,ul=0):
    counter=0
    if ul==1:
        for i in range(len(inp)):
            asc_val=ord(inp[i]) # convert to ASC value
            # an uppercase character has ASC value in range [65;90]
            validation=(asc_val>=65)*(asc_val<=90)
            if validation:
                counter +=1
    else:
        for i in range(len(inp)):
            asc_val=ord(inp[i]) # convert to ASC value
            # an uppercase character has ASC value in range [97;122]
            validation=(asc_val>=97)*(asc_val<=122)
            if validation:
                counter +=1
    return counter

# Reverse the string
def reverse(inp):
    rev_str=''
    for i in range(len(inp)):
        rev_ind=len(inp)-i-1 # reversing index
        rev_str += inp[rev_ind]
    return rev_str

def string_stats(inp):
    count_a =0
    count_0 =0
    count_s =0
    for i in range(len(inp)):
        asc_val=ord(inp[i]) # convert to ASC value
        if (asc_val>=65)*(asc_val<=90)+(asc_val>=97)*(asc_val<122):
            count_a +=1
        elif (asc_val>=48)*(asc_val<=57): # for numeric character
            count_0 +=1
        elif asc_val==32: # it does not count space character
            continue
        else:
            count_s +=1
    print('Number of alphabet character is ',count_a)
    print('Number of numeric character is ',count_0)
    print('Number of special character is ',count_s)
    
#Main Program
sta_tim= tm.time()
exa_inp_0='I will complete MSDS in one year.'
exa_inp_1='lets you choose #CleanPower for NO \
additional cost! IT IS A NO-BRAINER!!!'
exa_inp_2='Tesla software V10 is lookin real good! \
Releasing to early access list soon …'
inp=exa_inp_2
#inp=input('Please enter your tweet: ')
print('Information of string : ',inp)
print('The number of word in that string is :',word_counter(inp))
print('The average number of letter is : ',ave_nol(inp))
print('The number of uppercase letter is :',count_ul_cha(inp,1))
print('The number of lowercase letter is :',count_ul_cha(inp))
print('The reserve of that string is :',reverse(inp))
string_stats(inp)
end_tim=tm.time()
com_tim=end_tim-sta_tim
print('Computing time is',com_tim)