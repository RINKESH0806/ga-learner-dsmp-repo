# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
#print(data)
census=np.concatenate((data,new_record))
print(census)


# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)


# --------------
#Code starts here
race=census[:,2]
#print(race)
race_0=census[race == 0]
#print(race_0)
race_1=census[race == 1]
#print(race_1)
race_2=census[race == 2]
#print(race_2)
race_3=census[race == 3]
#print(race_3)
race_4=census[race == 4]
#print(race_4)
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)
minority_race=3
print(minority_race)


# --------------
#Code starts here
senior_citizens=census[age>60]
#print(senior_citizens)
working_hours=senior_citizens[:,6]
#print(working_hours)
working_hours_sum=working_hours.sum()
#print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
edu_num=census[:,1]
high=census[edu_num>10]
low=census[edu_num<=10]
avg_pay_high=np.mean(high[:,7])
print(avg_pay_high)
avg_pay_low=np.mean(low[:,7])
print(avg_pay_low)
#comp=np.compare(avg_pay_high,avg_pay_low) is wrong
#print(comp)


