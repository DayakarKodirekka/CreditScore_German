import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict, retrain
from typing import List

# defining the main app
app = FastAPI(title="Credit Loan Predictor", docs_url="/")

# calling the load_model during startup.
# this will train the model and keep it loaded for prediction.
app.add_event_handler("startup", load_model)

# class which is expected in the payload
class QueryIn(BaseModel):

    # Status_of_existing_checking_account: str
    # Duration_in_month:float
    # Credit_history: float
    # Purpose: str
    # Credit_amount: float
    # Savings_account: str
    # Present_employment: str
    # Installment_rate_in_percentage_of_disposable_income: float
    # Personal_status_and_sex:str
    # Other_debtors_guarantors:str # remove the blackslash from the column
    # Present_residence_since:float
    # Property:str
    # Age_in_years:float
    # Other_installment_plans:str
    # Housing:str
    # Number_of_existing_credits_at_this_bank:float
    # Job:str
    # Number_of_people_being_liable_to_provide_maintenance_for:float
    # Telephone:str
    # foreign_worker:str

    Status_of_existing_checking_account: any
    Duration_in_month:float
    Credit_history: float
    Purpose: any
    Credit_amount: float
    Savings_account: any
    Present_employment: any
    Installment_rate_in_percentage_of_disposable_income: float
    Personal_status_and_sex:any
    Other_debtors_guarantors:any # remove the blackslash from the column
    Present_residence_since:float
    Property:any
    Age_in_years:float
    Other_installment_plans:any
    Housing:any
    Number_of_existing_credits_at_this_bank:float
    Job:any
    Number_of_people_being_liable_to_provide_maintenance_for:float
    Telephone:any
    foreign_worker:any
    


# class which is returned in the response
class QueryOut(BaseModel):
      risk:str # remove the "()" from the column

# class which is expected in the payload while re-training
class FeedbackIn(BaseModel):
    # Status_of_existing_checking_account: str
    # Duration_in_month:float
    # Credit_history: float
    # Purpose: str
    # Credit_amount: float
    # Savings_account_bonds: str
    # Present_employment: str
    # Installment_rate_in_percentage_of_disposable_income: float
    # Personal_status_and_sex:str
    # Other_debtors_guarantors:str # remove the blackslash from the column
    # Present_residence_since:float
    # Property:str
    # Age_in_years:float
    # Other_installment_plans:str
    # Housing:str
    # Number_of_existing_credits_at_this_bank:float
    # Job:str
    # Number_of_people_being_liable_to_provide_maintenance_for:float
    # Telephone:str
    # foreign_worker:str
    # risk:str

    Status_of_existing_checking_account: any
    Duration_in_month:float
    Credit_history: float
    Purpose: any
    Credit_amount: float
    Savings_account: any
    Present_employment: any
    Installment_rate_in_percentage_of_disposable_income: float
    Personal_status_and_sex:any
    Other_debtors_guarantors:any # remove the blackslash from the column
    Present_residence_since:float
    Property:any
    Age_in_years:float
    Other_installment_plans:any
    Housing:any
    Number_of_existing_credits_at_this_bank:float
    Job:any
    Number_of_people_being_liable_to_provide_maintenance_for:float
    Telephone:any
    foreign_worker:any
    risk:any

# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    return {"ping": "pong"}


@app.post("/predict_loan", response_model=QueryOut, status_code=200)
# Route to do the prediction using the ML model defined.
# Payload: QueryIn containing the parameters
# Response: QueryOut containing the flower_class predicted (200)
def predict_loan(query_data: QueryIn):
    output = {"risk": predict(query_data)}
    return output

@app.post("/feedback_loop", status_code=200)
# Route to further train the model based on user input in form of feedback loop
# Payload: FeedbackIn containing the parameters and correct flower class
# Response: Dict with detail confirming success (200)
def feedback_loop(data: List[FeedbackIn]):
    retrain(data)
    return {"detail": "Feedback loop successful"}


# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8888
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)