from fastapi.testclient import TestClient
from main import app
# from datatime import datetime

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_loan():
    # defining a sample payload for the testcase
    payload = {
        "Status_of_existing_checking_account": "A11",
        "Duration_in_month": 24,
        "Credit_history": "A33",
        "Purpose": "A40",
        "Credit_amount": 4870,
        "Savings_account": "A61",
        "Present_employment": "A73",
        "Installment_rate_in_percentage_of_disposable_income": 3,
        "Personal_status_and_sex": "A93",
        "Other_debtors_guarantors": "A101",
        "Present_residence_since": 4,
        "Property": "A124",
        "Age_in_years": 53,
        "Other_installment_plans": "A143",
        "Housing": "A153",
        "Number_of_existing_credits_at_this_bank": 1,
        "Job": "A173",
        "Number_of_people_being_liable_to_provide_maintenance_for": 2,
        "Telephone":"A191",
        "foreign_worker": "A201",
    }
    with TestClient(app) as client:
        response = client.post("/predict_loan", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"risk": "Good"}
        # print(datatime.strftime("%H:%M:%S.%f",response.elapsed.total_seconds()))




