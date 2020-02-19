# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
df=pd.read_csv(path)
#print(df.head(), df.info)

col=['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']

for c in col:

    df[c] = df[c].str.replace("$", "")
    df[c] = df[c].str.replace(",", "")

y=df['CLAIM_FLAG']
X=df.drop('CLAIM_FLAG',axis=1)

count=y.value_counts()

print(count)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


# Code ends here


# --------------
# Code starts here
X_train[col]=X_train[col].astype(float)
X_test[col]=X_test[col].astype(float)

print(X_train.isnull().sum())
print(X_test.isnull().sum())
# Code ends here


# --------------
# Code starts here
X_train.dropna(subset=['YOJ','OCCUPATION'], inplace=True)
X_test.dropna(subset=['YOJ','OCCUPATION'], inplace=True)

y_train= y_train[X_train.index]
y_test= y_test[X_test.index]

X_train['AGE'].fillna((X_train['AGE'].mean()), inplace=True)
X_train['CAR_AGE'].fillna((X_train['CAR_AGE'].mean()), inplace=True)
X_train['INCOME'].fillna((X_train['INCOME'].mean()), inplace=True)
X_train['HOME_VAL'].fillna((X_train['HOME_VAL'].mean()), inplace=True)

X_test['AGE'].fillna(( X_test['AGE'].mean()), inplace=True)
X_test['CAR_AGE'].fillna(( X_test['CAR_AGE'].mean()), inplace=True)
X_test['INCOME'].fillna(( X_test['INCOME'].mean()), inplace=True)
X_test['HOME_VAL'].fillna(( X_test['HOME_VAL'].mean()), inplace=True)  
# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
le= LabelEncoder()

for x in columns:
    X_train[x]= le.fit_transform(X_train[x].astype(str))
    X_test[x]= le.transform(X_test[x].astype(str))
# Code ends here




# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# code starts here 
model= LogisticRegression(random_state=6)
model.fit(X_train, y_train)

y_pred= model.predict(X_test)
score= accuracy_score(y_test, y_pred)
print(score)
# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
smote= SMOTE(random_state=9)
X_train, y_train= smote.fit_sample(X_train, y_train)

scaler= StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)
# Code ends here


# --------------
# Code Starts here
model=LogisticRegression()

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

score=accuracy_score(y_pred,y_test)
print(score)

# Code ends here


