import pandas as pd
import numpy as np
from error import rmse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier


data = pd.read_csv("Data.csv")


''' Matrix initialization '''
col = 3
row = 943 * 1682

Initiated_Array = np.zeros((row,col))
#print(Initiated_Array)



'''For Normalization '''
min_rating = min(data["Rating"]) 
max_rating = max(data["Rating"])



X=data[['User','Item']]      #Independent Variables
y=data['Rating']

'''Min-Max Normalization on Y'''
Y=data['Rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values   #Dependent variable


train_x, test_x, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=42)


'''1. LinearRegression Model'''
print("\n\n")
print("**************** LinearRegression Model ****************")
reg = LinearRegression()
reg.fit(train_x, train_Y)

predicted_L = reg.predict(test_x)
print('Model Score: ',reg.score(test_x, test_Y))

'''RMSE Value for Predicted'''
print('RMSE value for LinearRegression Model : ', rmse(predicted_L, test_Y))


'''
users =  943
items = 1682
ratings = 0#1682

print("\n")
print("Predicting the values....")
Final_Ratings_1 = []

for i in range(845,users+1):    
    for j in range(1500,items+1):
        rating = reg.predict([[i,j]])
        Actual_rating = ( rating * (max_rating - min_rating)) + min_rating
        Final_Ratings_1.append(int(Actual_rating))

print("\n")
print(Final_Ratings_1)      
'''




'''2. Random Forest Model'''
print("\n\n")
print("**************** Random Forest Model ****************")
regr_R = RandomForestRegressor(max_depth=2, random_state=0)
regr_R.fit(train_x, train_Y)

predicted_R = regr_R.predict(test_x)
print('Model Score: ',regr_R.score(test_x, test_Y))

'''RMSE Value for Predicted'''
print('RMSE value for Random Forest Model : ', rmse(predicted_R, test_Y))
print("\n\n")


'''
The matrix has 943 users (m = 943) and 1682 items (n = 1682).
Your goal is to fill out all the entries of this matrix with the current value as 0 (or no value yet). 

'''
'''
users =  943
items = 1682
ratings = 0#1682

print("\n")
print("Predicting the values....")
Final_Ratings = []

for i in range(845,users+1):    
    for j in range(1500,items+1):
        rating = regr_R.predict([[i,j]])
        Actual_rating = ( rating * (max_rating - min_rating)) + min_rating
        Final_Ratings.append(int(Actual_rating))

print("\n")
print(Final_Ratings)      
'''
#Actual_Y = (model.predict([[209,260]]) * (max_rating - min_rating)) + min_rating


'''3. Logistic Regression Model'''


train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42) # Without Normalization 

print("\n\n")
print("**************** Logistic Regression Model ****************")
l_reg = LogisticRegression(random_state=0)
l_reg.fit(train_x, train_y)

predicted_l_reg = l_reg.predict(test_x)
print('Model Score: ',l_reg.score(test_x, test_y))

'''RMSE Value for Predicted'''
print('RMSE value for Random Forest Model : ', rmse(predicted_l_reg, test_y))
print("\n\n")




'''4. KNN Clustering Classifier '''

print("\n\n")
print("**************** KNN Model ****************")
neigh = KNeighborsClassifier()
neigh.fit(train_x, train_y)

predicted_K = neigh.predict(test_x)
print('Model Score: ',neigh.score(test_x, test_y))

'''RMSE Value for Predicted'''
print('RMSE value for Random Forest Model : ', rmse(predicted_K, test_y))
print("\n\n")



users =  10 #943
items = 15 #1682
ratings = 0#1682

print("\n")
print("Predicting the ratings given for 15 items by 10 users  ....")
Predicted_Ratings = []

for i in range(1,users+1):    
    for j in range(1,items+1):
        rating = neigh.predict([[i,j]])
        #Actual_rating = ( rating * (max_rating - min_rating)) + min_rating
        Predicted_Ratings.append(int(rating))

print("\n")
print("Predicted Ratings are : ",Predicted_Ratings)
print("\n")