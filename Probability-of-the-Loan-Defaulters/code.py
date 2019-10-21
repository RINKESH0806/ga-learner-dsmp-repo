# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
#print(df.head())
total_count=len(df)
df_of_700fico=len(df[df['fico']>700])
p_a=df_of_700fico/total_count
print(p_a)
df_of_debt=len(df[df['purpose']=='debt_consolidation'])
p_b=df_of_debt/total_count
print(p_b)

df1=df[df['purpose']=='debt_consolidation']
df1_of_700fico=len(df1[df1['fico']>700])
p_a_b=df1_of_700fico/len(df1)
print(p_a_b)
result=p_a_b==p_a
print(result)

# code ends here


# --------------
# code starts here
prob_lp=len(df[df['paid.back.loan']=='Yes'])/len(df)
print(prob_lp)
prob_cs=len(df[df['credit.policy']=='Yes'])/len(df)
print(prob_cs)
new_df=df[df['paid.back.loan']=='Yes']
prob_pd_cs=len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
print(prob_pd_cs)
bayes=prob_pd_cs*prob_lp/prob_cs
print(bayes)

# code ends here


# --------------
# code starts here
plt.bar(df['purpose'],100)
plt.show()
df1=df[df['paid.back.loan']=='No']
plt.bar(df1['purpose'],100)
plt.show()
# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
plt.hist(df['installment'])
plt.show()
plt.hist(df['log.annual.inc'])
plt.show
# code ends here


