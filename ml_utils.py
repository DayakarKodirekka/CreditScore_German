# Importing and loading the required packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# from collections import Counter
# import gdown

import copy
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import fbeta_score, f1_score,precision_score,recall_score,accuracy_score, roc_curve, auc
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')
from credit_data_actual_values import substitute

# define a Random Forest Classifier
clf = RandomForestClassifier()

# define the class encodings and reverse encodings
classes = {1: "Good", 2: "Bad"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def load_model():

    # loading the dataset
    #Load the data using pandas read_csv method
    df= pd.read_csv('./output.csv', sep=" ",names=['Status_of_existing_checking_account', 'Duration_in_month','Credit_history', 'Purpose', 'Credit_amount', 'Savings_account','Present_employment','Installment_rate_in_percentage_of_disposable_income','Personal_status_and_sex','Other_debtors_guarantors','Present_residence_since','Property','Age_in_years','Other_installment_plans', 'Housing','Number_of_existing_credits_at_this_bank','Job','Number_of_people_being_liable_to_provide_maintenance_for', 'Telephone','foreign_worker', 'risk'])
    # split the data frame into inputs and outputs
    last_ix = len(df.columns) - 1
    X, y = df.drop(last_ix, axis=1), df[last_ix]

    # do the test-train split and train the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf.fit(X_train, y_train)

    # calculate the print the accuracy score
    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"Model trained with accuracy (Random Forest): {round(acc, 3)}")


# function to predict the flower using the model
def predict(query_data):
    x = list(query_data.dict().values())
    prediction = clf.predict([x])[0]
    print(f"Model prediction: {classes[prediction]}")
    return classes[prediction]

# function to retrain the model as part of the feedback loop
def retrain(data):
    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.risk] for d in data]

    # fit the classifier again based on the new data obtained
    clf.fit(X, y)

