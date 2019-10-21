# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar')
plt.show()



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

alignment_types = 'good','bad','neutral'

plt.pie(alignment,labels = alignment_types,startangle=90,shadow=True)

plt.title('Character Alignment')

plt.show()


# --------------
#Code starts here
data = pd.read_csv(path)

sc_df = data[['Strength','Combat']]

sc_covariance = round(sc_df.cov().iloc[0,1],2)

print(sc_covariance)

sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance / (sc_strength * sc_combat)

ic_df = data[['Intelligence','Combat']]

ic_covariance = round(ic_df.cov().iloc[0,1],2)
print(ic_covariance)

ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance / (ic_intelligence*ic_combat)


print(sc_pearson)
print(ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)

print(total_high)

super_best = data[data['Total'] > total_high]

print(super_best)

super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here
fig , (ax_1,ax_2,ax_3) = plt.subplots(3,figsize=(15,15))

data.boxplot(column='Intelligence',ax=ax_1)

ax_1.set_title('Intelligence')

ax_2 = data.boxplot(column='Speed',ax=ax_2)
 
ax_2.set_title('Speed')

ax_3 = data.boxplot(column = 'Power',ax=ax_3)

ax_3.set_title('Power')


