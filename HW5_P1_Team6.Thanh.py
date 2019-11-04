# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:35:22 2019

@author: Duong Hung
"""
# A function to calculate 3 statistical information of an array
import numpy as np
def stat_inf(dat):
    mea=round(np.mean(dat),2)
    sd=round(np.std(dat),2)
    med=round(np.median(dat),2)
    return [[mea,sd,med]]

#Import data from file
fname='insurance.txt'
feats=('age','sex','bmi','children','smoker','region','expenses')
#Define type for each features
typ_f=('i2','U7','f2','i2','U3','U9','f4')
data=np.loadtxt(fname,dtype={'names': feats,'formats': typ_f},skiprows=1)

# Prepare for output
ofname='HW5_results.txt'
results=np.empty((0,3))

#1. Mean, sd and median of age
results=np.append(results,stat_inf(data['age']),axis=0)

#2. Mean, sd and median of bmi
results=np.append(results,stat_inf(data['bmi']),axis=0)

#3. Mean, sd and median of bmi by group of sex
att=np.unique(data['sex']) # find unique value in sex column
for val in att:
    bmi_g=data['bmi'][data['sex']==val]
    results=np.append(results,stat_inf(bmi_g),axis=0)
    
#4. Mean, sd and median of bmi for smoker and non smoker
att=np.unique(data['smoker'])
for val in att:
    bmi_g=data['bmi'][data['smoker']==val]
    results=np.append(results,stat_inf(bmi_g),axis=0)

#5.Mean, sd and median of bmi grouped by region
att=np.unique(data['region'])
for val in att:
    bmi_g=data['bmi'][data['region']==val]
    results=np.append(results,stat_inf(bmi_g),axis=0)
    
#6 Mean, sd and median of bmi of those who have more than 2 children
bmi_g=data['bmi'][data['children']>2]
results=np.append(results,stat_inf(bmi_g),axis=0)

# Write results to a file
np.savetxt(ofname,results,fmt='%.4f')

att=np.unique(data['children'])
for val in att:
    bmi_g=data['bmi'][data['children']==val]
    print('\nFor the group that have ',val,' children')
    print('Mean =',np.mean(bmi_g), 'SD =',np.std(bmi_g), 
          ' and median =',np.median(bmi_g) )
''' How the following factors affect BMI '''
'''1. Smoking habit'''
'''It seem that people that does not smoke has slightly lower BMI than the ones who smokes.
but the different is no significant because the sd is around 6 and the abs difference of means of
2 group is around 0.06'''
'''2. Region 
people live in north seems to have lower BMI than people live in the south. 
Northwest people has the highest mean of BMI'''

'''3. Children
As number of children increase, the BMI index increase. and it reachs the peak at 4 kids. 
After that, BMI decrease to the lowest.'''


'''What are the primary reasons for the top 20% of the expenses? 
In particular, sort the data by expense, and compute the mean,
 and standard deviation of BMI and the mode of smoker and region. 
 How do these values differ from the rest 80% of the population? 
 '''
ex_data=np.sort(data, order='expenses') # sort by expensese
div_ind=int(np.floor(data.shape[0]*0.8)) # index to split the data 80/20
dat_be, dat_te=np.split(ex_data,[div_ind]) # split data into 2 group

print('\nFor 20% of the expenses, ')
print('BMI factor has Mean =',np.mean(dat_te['bmi']), 'SD =',np.std(dat_te['bmi']), 
          ' and median =',np.median(dat_te['bmi']) )
ele,cou=np.unique(dat_te['smoker'],return_counts=True)
print('The frequency of smoker is')
print(ele)
print(cou)
print('- The primary smoker status is',ele[np.argmax(cou)])
ele,cou=np.unique(dat_te['region'],return_counts=True)
print('The frequency of region is')
print(ele)
print(cou)
print('- The primary region status is',ele[np.argmax(cou)])

print('\nFor the rest of population, ')
print('BMI factor has Mean =',np.mean(dat_be['bmi']), 'SD =',np.std(dat_be['bmi']), 
          ' and median =',np.median(dat_be['bmi']) )
ele,cou=np.unique(dat_be['smoker'],return_counts=True)
print('The frequency of smoker is')
print(ele)
print(cou)
print('- The primary smoker status is',ele[np.argmax(cou)])
ele,cou=np.unique(dat_be['region'],return_counts=True)
print('The frequency of region is')
print(ele)
print(cou)
print('- The primary region status is',ele[np.argmax(cou)])
