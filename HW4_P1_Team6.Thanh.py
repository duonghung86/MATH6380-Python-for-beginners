# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:12:12 2019

@author: Duong Hung
"""
import numpy as np

#Main
fil_nam='WorldSeriesWinners.txt'
year=np.arange(1903,2010)
year=year[[x!=1904 and x!= 1994 for x in year]]
fhand=open(fil_nam)
team_year={}
#team=list()
i=0
for line in fhand:
    #three ways to remove New line in a string
    #name=line[:len(line)-1]
    #name=line.replace('\n', '')
    name=line.translate({ord('\n'): None})
    #verify whether the team name already is stored in dict or not
    # If it haven't been stored yet
    if name not in team_year:
        #then append it
        team_year[name]=[year[i]]    
    else:
        #add the year number to the value of the team
        team_year[name].append(year[i])
    i+=1    

#print(team_year)
def take_second(elem):
    return elem[1]

#Sort the team after alphabet
#Convert dictionary to list
win_lis = list(team_year.items()) #number of win list

# Sort in descending order 
win_lis.sort()
for key, val in win_lis:
    print(key,':',val)

print('===================================================')
#Create another dictionary in which keys are the team names 
#and values are the occurrence of win
team_win={}
team_year=dict(win_lis)
for key in team_year:
    team_win[key]=len(team_year[key])
    print(key,':',team_win[key])
#print(team_win)
print('===================================================')
#Sort the team after number of win
#Convert dictionary to list
win_lis = list(team_win.items()) #number of win list
# Sort in descending order 
win_lis.sort(key=take_second, reverse=True)
for key, val in win_lis:
    print(key,'(',val,'):','*'*val)

