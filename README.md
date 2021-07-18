# CreditScore_German

--- This solution is deveopled in jupter notebook---
# Building model for credit score data 
    * Downloaded the reuired dataset
    * Displayed top 5 records of the dataset
    * Checked for null values - found none
    * Visualized the data by plotting bar charts
    * plotted Correlation matrix
    * Categorical features are converted into numerical data using onehot encoder
## Imbalance in the data
    * Used SMOTE(Synthetic Minority Oversampling Technique) model to remove the imbalnce in the data
## Modeling
* Trained the model with differnt classifiers
    * Random Forest
    * Logistic Regression
    * Decision Tree
## Evaluation
    * evaluated the model for the above model
    * random forest is having higher accuracy and f1-score



# MlOps - 
## Running Instructions
- Create a fork of the repo using the `fork` button.
- Clone your fork using `git clone https://github.com/DayakarKodirekka/CreditScore_German.git`
- Install dependencies using `pip3 install -r requirements.txt`
- Run application using `python3 main.py`
- Run tests using `pytest`

## CI/CD
- `build` (test) for all the pull requests
- `build` (test) and `upload_zip` for all pushes