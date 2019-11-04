# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:47:20 2019

@author: Duong Hung
"""
import time as tm
import numpy as np

sta_tim=tm.time()
# Read file
fhand=open('steps.txt')
data=fhand.read()
fhand.close()

data=data.split('\n')

#Establish a matrix 12x31 
# 12 is the number of months
# 31 is the maximum number of days in a month
max_ste=np.zeros((12,31))
#Number of days in each month
nod=[31,28,31,30,31,30,31,31,30,31,30,31]
j=0 # index of data
for i in range(12):
    day_mon=nod[i]
    sta_ind=sum(nod[:i]) # index for start of the month
    end_ind=sta_ind+nod[i] # index for end of the month
    while j<=end_ind-1:
        max_ste[i,j-sta_ind]=int(data[j])
        j+=1

#Set up array of average, min and max values for each month
anos=[0]*12
max_stp=[0]*12
min_stp=[0]*12
for i in range(12):
    anos[i]=round(sum(max_ste[i,])/nod[i],2) # average number of steps for each month
    max_stp[i]=int(max(max_ste[i,])) # smallest number of steps for each month
    min_stp[i]=int(min(max_ste[i,:nod[i]])) # largest number of steps for each month

#Output
print('Month    Average    Minimum    Maximum')
print('======================================')
for i in range(12):
    # use k - len(str()) to align the numbers
    print(i+1,' '*(7-len(str(i+1))),anos[i],' '*(9-len(str(anos[i]))),
          min_stp[i],' '*(9-len(str(min_stp[i]))),max_stp[i])
  

end_tim=tm.time()
com_tim=end_tim-sta_tim
print('Computing time is',com_tim)