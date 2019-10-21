# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df=pd.read_csv(path)
print(df.head())
X=df.drop(columns='list_price')
y=df['list_price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=6)
# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols=X_train.columns
fig,axes=plt.subplots(nrows = 3 , ncols = 3)
for i in range(0,3):
    for j in range(0,3):
        col=cols[i*3 + j]
        axes[i,j].plot(X_train[col],y_train)
        axes[i,j].set_xlabel(col)
        axes[i,j].set_ylabel('list_price')

       

# code ends here



# --------------
# Code starts here
import seaborn as sns

corr = X_train.corr()

sns.heatmap(corr,annot=True)

# features of play_star_rating, val_star_rating and star_ratin have a correlation of greater than 0.75.
# hence dropping these two columns to improve model efficiency.
X_train.drop(columns=['play_star_rating','val_star_rating'],inplace=True)

X_test.drop(columns=['play_star_rating','val_star_rating'],inplace=True)


# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Code starts here

regressor = LinearRegression()

regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
print(mse)

r2 =  r2_score ( y_test , y_pred)
print(r2)


# Code ends here


# --------------
# Code starts here
data = pd.DataFrame({'actual':y_test,'predicted':y_pred})
print(data)
residual = y_test - y_pred
print(residual)
residual.hist()
# Code ends here


