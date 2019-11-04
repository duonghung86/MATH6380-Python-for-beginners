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
res=dict()

#1. Mean, sd and median of age
results=np.append(results,stat_inf(data['age']),axis=0)
res['Age']=results[0]
#2. Mean, sd and median of bmi
results=np.append(results,stat_inf(data['bmi']),axis=0)
res['BMI']=results[1]
#3. Mean, sd and median of bmi by group of sex
att=np.unique(data['sex']) # find unique value in sex column
i=2
for val in att:
    bmi_g=data['bmi'][data['sex']==val]
    results=np.append(results,stat_inf(bmi_g),axis=0)
    rownam='BMI - '+val 
    res[rownam]=results[i]
    i+=1
#4. Mean, sd and median of bmi for smoker and non smoker
att=np.unique(data['smoker'])
for val in att:
    bmi_g=data['bmi'][data['smoker']==val]
    results=np.append(results,stat_inf(bmi_g),axis=0)
    rownam='BMI - smoking - '+val 
    res[rownam]=results[i]
    i+=1

#5.Mean, sd and median of bmi grouped by region
att=np.unique(data['region'])
for val in att:
    bmi_g=data['bmi'][data['region']==val]
    results=np.append(results,stat_inf(bmi_g),axis=0)
    rownam='BMI - region - '+val
    res[rownam]=results[i]
    i+=1
    
#6 Mean, sd and median of bmi of those who have more than 2 children
bmi_g=data['bmi'][data['children']>2]
results=np.append(results,stat_inf(bmi_g),axis=0)
rownam='BMI - #children > 2'
res[rownam]=results[i]
# Extra. Mean, sd and median of bmi grouped by number of children
att=np.unique(data['children'])
for val in att:
    bmi_g=data['bmi'][data['children']==val]
    rownam='BMI - #children = '+str(val)
    res[rownam]=stat_inf(bmi_g)
    
# Write results to a file
np.savetxt(ofname,results,fmt='%.4f')
# Print the result with names
for key, value in res.items():
    print(f'{key:30}{value}')

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
