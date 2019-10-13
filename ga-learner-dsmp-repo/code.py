# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank=pd.read_csv(path)
#print(bank)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)

# code starts here






# code ends here


# --------------
# code starts here
banks=bank.drop(['Loan_ID'],axis=1)
#print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
#print(bank_mode)
banks.fillna(bank_mode,inplace=True)
#print(banks)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here
loan_approved_se=banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].shape[0]
print(loan_approved_se)
loan_approved_nse=banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].shape[0]
print(loan_approved_nse)
percentage_se=(loan_approved_se/614)*100
print(percentage_se)
percentage_nse=(loan_approved_nse/614)*100
print(percentage_nse)
# code ends here


# --------------
# code starts here
banks['loan_term']=banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
loan_term=banks['loan_term']
print(len(loan_term))
big_loan_term=len(banks[banks['loan_term']>=25])
print(big_loan_term)

# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
mean_values=loan_groupby.mean()
print(mean_values)

# code ends here


