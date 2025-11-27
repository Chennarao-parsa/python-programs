import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os
print(os.listdir())

import warnings
warnings.filterwarnings('ignore')
dataset = pd.read_csv("heart.csv")
print("Dataset type:", type(dataset))
print("Dataset shape:", dataset.shape)
print("First 5 rows of the dataset:")
print(dataset.head(5))
print("Random sample of 5 rows from the dataset:")
print(dataset.sample(5))
print("Summary statistics of the dataset:")
print(dataset.describe())
print("Information about the dataset:")
print(dataset.info())
info = ["age","1: male, 0: female","chest pain type, 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic","resting blood pressure"," serum cholestoral in mg/dl","fasting blood sugar > 120 mg/dl","resting electrocardiographic results (values 0,1,2)"," maximum heart rate achieved","exercise induced angina","oldpeak = ST depression induced by exercise relative to rest","the slope of the peak exercise ST segment","number of major vessels (0-3) colored by flourosopy","thal: 3 = normal; 6 = fixed defect; 7 = reversable defect"]



from sklearn.model_selection import train_test_split

predictors = dataset.drop("target",axis=1)
target = dataset["target"]

X_train,X_test,Y_train,Y_test = train_test_split(predictors,target,test_size=0.20,random_state=0)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("Y_train shape:", Y_train.shape)
print("Y_test shape:", Y_test.shape)


from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

param_grid = {'random_state': range(10)}  # try 10 different random states
rf = RandomForestClassifier()
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, Y_train)

print("Best parameters:", grid_search.best_params_)
print("Best accuracy:", grid_search.best_score_)

rf_best = grid_search.best_estimator_
Y_pred_rf = rf_best.predict(X_test)
score_rf = round(accuracy_score(Y_pred_rf, Y_test) * 100, 2)

print("The accuracy score achieved using Random Forest is: " + str(score_rf) + " %")
scores = [score_rf]
algorithms = ["Random Forest"]    

for i in range(len(algorithms)):
    print("The accuracy score achieved using " + algorithms[i] + " is: " + str(scores[i]) + " %")


sns.set(rc={'figure.figsize':(15,8)})
plt.xlabel("Algorithms")
plt.ylabel("Accuracy score")

sns.barplot(x=algorithms, y=scores, palette=["green", "red"])  # changed to green and red
plt.show()