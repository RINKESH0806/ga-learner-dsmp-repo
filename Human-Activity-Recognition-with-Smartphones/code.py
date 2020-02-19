# --------------
import pandas as pd
from collections import Counter

# Load dataset
data = pd.read_csv(path)
print(data.isnull().sum())

print(data.describe())


# --------------
import seaborn as sns
from matplotlib import pyplot as plt
sns.set_style(style='darkgrid')

# Store the label values 
label= data['Activity'].copy()
chart= sns.countplot(x=label, data=data)
chart.set_xticklabels(chart.get_xticklabels(), rotation=90)

# plot the countplot



# --------------
# make the copy of dataset
data_copy= data.copy()

# Create an empty column 
data_copy['duration']= pd.Series()

# Calculate the duration
duration_df= (data_copy.groupby([label[(label=='WALKING_UPSTAIRS')|(label=='WALKING_DOWNSTAIRS')], 'subject'])['duration'].count() * 1.28)

duration_df= pd.DataFrame(duration_df)
print(duration_df.head())

# Sort the values of duration
plot_data= duration_df.reset_index().sort_values('duration', ascending= False)
plot_data['Activity']= plot_data['Activity'].map({'WALKING_UPSTAIRS': 'Upstairs', 'WALKING_DOWNSTAIRS': 'Downstairs'})

plt.figure(figsize=(14,4))
sns.barplot(data=plot_data, x='subject', y='duration', hue='Activity')
plt.show()


# --------------
#exclude the Activity column and the subject column
feature_cols= data.columns[:-2]

#Calculate the correlation values
correlated_values= data[feature_cols].corr()

#stack the data and convert to a dataframe
correlated_values= correlated_values.stack().to_frame().reset_index()
correlated_values = correlated_values.rename(columns={'level_0':'Feature_1', 'level_1':'Feature_2', 0:'Correlation_score'})
print(correlated_values.head())

#create an abs_correlation column
correlated_values['abs_correlation']= correlated_values['Correlation_score'].abs()

s_corr_list= correlated_values.sort_values('abs_correlation', ascending= False)
print(s_corr_list.head())

#Picking most correlated features without having self correlated pairs
top_corr_fields= s_corr_list[s_corr_list['abs_correlation']>0.8]
# print(top_corr_feilds.head())

top_corr_fields= top_corr_fields[top_corr_fields['Feature_1']!=top_corr_fields['Feature_2']].reset_index(drop= True)
print(top_corr_fields.head())




# --------------
# importing neccessary libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_fscore_support as error_metric
from sklearn.metrics import confusion_matrix, accuracy_score

# Encoding the target variable
le = LabelEncoder()
data['Activity'] = le.fit_transform(data.Activity)
X = data.iloc[:,:-1]    
y = data.iloc[:,-1]

# split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Baseline model 
classifier = SVC()
clf = classifier.fit(X_train, y_train)
y_pred = clf.predict(X_test)
precision, recall, f_score, _ = error_metric(y_test, y_pred, average = 'weighted')
model1_score = accuracy_score(y_test, y_pred)
print(model1_score)
print(precision, recall, f_score)




# --------------
# importing libraries
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

# Feature selection using Linear SVC
lsvc= LinearSVC(C=0.01, penalty= 'l1', dual= False, random_state= 42)
model_2= SelectFromModel(lsvc, prefit= True)
print(X_train.shape)

lsvc.fit(X_train, y_train)
new_train_features= model_2.transform(X_train)
new_test_features= model_2.transform(X_test)
print(new_train_features.shape)

# model building on reduced set of features
classifier_2= SVC()
clf_2= classifier_2.fit(new_train_features, y_train)
y_pred_new= clf_2.predict(new_test_features)

model2_score= accuracy_score(y_test, y_pred_new)
print(model2_score)
precision, recall, f_score, support= error_metric(y_test, y_pred_new, average= 'weighted')
print(precision, recall, f_score, support)




# --------------
# Importing Libraries
from sklearn.model_selection import GridSearchCV

# Set the hyperparmeters
parameters= {'kernel': ['linear', 'rbf'], 'C': [100, 20, 1, 0.1], }
selector= GridSearchCV(SVC(), parameters, scoring= 'accuracy')

# Usage of grid search to select the best hyperparmeters
selector.fit(new_train_features, y_train)
print('Best HyperParam: ', selector.best_params_)

mean= selector.best_score_
means= selector.cv_results_['mean_test_score']
stds= selector.cv_results_['std_test_score']
std= selector.cv_results_['std_test_score'][selector.best_index_]

for m, s, p in zip(means, stds, selector.cv_results_['params']):
    print('%0.3f (+/-%0.03f) for %r' % (m, s * 2, p))
    print('-'*20)

print(mean, std)
# Model building after Hyperparameter tuning
best_ker= selector.best_params_['kernel']
best_c= selector.best_params_['C']
print('-'*30)
print(best_c, best_ker)

classifier_3= SVC(kernel=best_ker , C=best_c)
clf_3= classifier_3.fit(new_train_features, y_train)
y_pred_final= clf_3.predict(new_test_features)

model3_score= accuracy_score(y_test, y_pred_final)
print(model3_score)
precision, recall, f_score, support= error_metric(y_test, y_pred_final, average= 'weighted')
print(precision, recall, f_score, support)




