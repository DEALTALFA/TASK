#!/usr/bin/python3

import pandas,numpy,joblib
from sklearn.linear_model import LinearRegression
dataS=pandas.read_csv("Salary_Data.csv")
print(dataS.columns)
X=dataS["YearsExperience"].values.reshape(-1,1)
print(X)
Y=dataS["Salary"]
mind=LinearRegression()
model=mind.fit(X,Y)
do="yes"
#saving model
joblib.dump(model,'salary_pred.pk1')
#while(do=="yes"):
#    yr=int(input("Enter the year of experience:"))
#    model_load=joblib.load("salary_pred.pk1")
#    pred_salary=model_load.predict([[yr]])
#    print("Your salary predicted respective to the experience is:",pred_salary)
#    do=input("Want to predict more (yes/no)")

