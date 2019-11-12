# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
# Plotting a histogram of Rating column to see the distribution of app ratings
data['Rating'].hist()
# from the plotted histogram that there exists Rating>5 which shouldn't be there
data = data[data['Rating'] <= 5]
# histogram of Rating column again to see the distribution of app ratings
data['Rating'].hist()
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null / data.isnull().count())
missing_data = pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)

# observation :- There are null values in only two columns and that too in very few rows. We can straight off drop the null values.

data.dropna(inplace=True)
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1 / data.isnull().count())
missing_data_1 = pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)

# observation :- There are no null values left in the data.

# code ends here


# --------------

#Code starts here

# Using seaborn, plotting the catplot to see relation between Rating and Category
sns.catplot(x='Category',y='Rating',data=data,kind="box",height=10)

plt.xticks(rotation=90)

plt.title('Rating vs Category [BoxPlot]')

# observation
# Rating of application in each category don't vary with each other much.



#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
# Removing , and + from Installs column of 'data'.
data['Installs'] = data['Installs'].str.replace(",","")
data['Installs'] = data['Installs'].str.replace("+","")

# converting Installs column to datatype int
data = data.astype({'Installs':int})

# creating labelencoder object to transform values of Installs column
le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

print(data['Installs'])

sns.regplot(x='Installs',y='Rating',data=data)

plt.title("Rating vs Installs [RegPlot]")
# Observations
# There is but a small positive correlation between number of installs and ratings




#Code ends here



# --------------
#Code starts here
# Checking value counts of price column
print(data['Price'].value_counts()) 
# Observations
# The column Price is not of type float
# Majority of the values is 0(More than 90%)
# Replacing '$' with ''
data['Price'] = data['Price'].str.replace("$","")
# Converting price column to float
data = data.astype({'Price':float})
# Plotting the regression plot for Price vs Ratings
sns.regplot(x='Price',y='Rating',data=data)
plt.title('Rating vs Price [RegPlot]')
#Code ends here


# --------------

#Code starts here
data['Genres'].unique()

# Observation
# The column Genres has 115 unique values
# Some of the apps have multiple genres hence resulting in 115 unique combinations

# Splitting values of columns Genres by ; and storing only first Genre
data['Genres'] = data['Genres'].str.split(';').str[0]

# Grouping Genres and Rating by Genres
gr_mean = data[['Genres','Rating']].groupby(by='Genres',as_index=False).mean()
print(gr_mean.describe())

# sorting the values by Rating
gr_mean = gr_mean.sort_values('Rating')
print(gr_mean)

# Observations-
# The lowest of average rating on genres (Dating) is 3.97
# The highest of average rating on genres (Events) is 4.43
# Owing to Standard Deviation of 0.1, seems like genre doesn't have much effect on rating




#Code ends here


# --------------

#Code starts here
# Printing to visualise the values of Last Updated column of 'data'
print(data['Last Updated'])
# Observation :- Last Updated column is not of the date type.

# Converting to datetime type
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

# Finding out max value in Last Update column
max_date = max(data['Last Updated'])
print(max_date)

# creating Last updated days column which is diff between max date and values of column last updated in days
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
sns.regplot(x='Last Updated Days',y='Rating',data=data)
plt.title('Rating vs Last Updated [RegPlot]')

# Observations- Higher the gap between the days last updated, lower the rating
#Code ends here


