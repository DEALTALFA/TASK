#!/usr/bin/python3

import joblib
model=joblib.load("salary_pred.pk1")
do="yes"
while(do=="yes"):
    yr=int(input("Enter the year of experience:"))
    pred_salary=model.predict([[yr]])
    print(f"Your salary predicted respective to the experience is:{pred_salary}")
    do=input("Want to predict more (yes/no)")
