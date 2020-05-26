import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

train_data = pd.read_csv('/mnt/train.csv')
test_data = pd.read_csv('/mnt/titanic_test.csv')
validation_data = pd.read_csv('/mnt/titanic_validation.csv')

age = train_data['Age']

def imputation(cols):
    age = cols[0]
    Pclass = cols[1]
    if pd.isnull(age):
        if Pclass == 1:
            return 38
        elif Pclass == 2:
            return 30
        elif Pclass == 3:
            return 25
        else:
            return 30
    else:
        return age

train_data['Age'] = train_data[['Age', 'Pclass']].apply(imputation, axis=1)

train_data['Age']
train_data.drop('Cabin', axis=1, inplace=True)

y_train = train_data['Survived']

x_train = train_data[['Age','Pclass', 'Sex',  'SibSp','Parch','Embarked']]

age = train_data['Age']

Pclass = train_data['Pclass']
Pclass = pd.get_dummies(Pclass, drop_first=True, prefix='Pclass')

Sibsp = train_data['SibSp']
Sibsp = pd.get_dummies(Sibsp, drop_first=True, prefix='Sibsp')

Parch = train_data['Parch']
Parch = pd.get_dummies(Parch, drop_first=True, prefix='Parch')

sex = train_data['Sex']
sex = pd.get_dummies(sex, drop_first=True, prefix='Sex')

embarked = train_data['Embarked']
embarked = pd.get_dummies(embarked, drop_first=True, prefix='Embarked')

x_train = pd.concat([age,Pclass, Sibsp, Parch, sex, embarked], axis=1)

x_test = test_data[['Age','Pclass', 'Sex',  'SibSp','Parch','Embarked']]

test_data['Age'] = test_data[['Age', 'Pclass']].apply(imputation, axis=1)
age = test_data['Age']

Pclass = test_data['Pclass']
Pclass = pd.get_dummies(Pclass, drop_first=True, prefix='Pclass')

Sibsp = test_data['SibSp']
Sibsp = pd.get_dummies(Sibsp, drop_first=True, prefix='Sibsp')

Parch = test_data['Parch']
Parch = pd.get_dummies(Parch, drop_first=True, prefix='Parch')

sex = test_data['Sex']
sex = pd.get_dummies(sex, drop_first=True, prefix='Sex')

embarked = test_data['Embarked']
embarked = pd.get_dummies(embarked, drop_first=True, prefix='Embarked')

x_test = pd.concat([age,Pclass, Sibsp, Parch, sex, embarked], axis=1)

x_test.drop('Parch_9', inplace=True, axis=1)

y_test = validation_data['Survived']

model = LogisticRegression()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

report = classification_report(y_test,y_pred)

report_new = report.split('\n')[-2]

accuracy = float(report_new.split()[2])*100

print("Your Accuracy is {}".format(accuracy))

joblib.dump(model,'/mnt/Logistic_regression.pk1')

import os
os.system("touch /mnt/accuracy.txt")
os.system("echo {} > /mnt/accuracy.txt".format(accuracy))
