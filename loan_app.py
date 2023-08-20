import pickle
from flask import Flask, request
import requests


app = Flask(__name__)

model = open("./classifier.pkl", "rb")
clf = pickle.load(model)


@app.route("/")
def welcome():
    return "<h1>Welcome...!!, </h1>" "<p>Please nevigate to ping page</p>"


@app.route("/ping")
def load_model():
    return "<h1>Loading the model, Please send post request to predict the results</h1>"


@app.route("/predict", methods=["POST"])
def predict():
    loan_req = request.get_json()

    # encoding parameters
    if loan_req["Gender"] == "Male":
        gender = 0
    else:
        gender = 1

    if loan_req["Married"] == "Unmarried":
        marital_status = 0
    else:
        marital_status = 1

    # Numerical parameters
    applicant_income = loan_req["ApplicantIncome"]
    loan_amount = (
        loan_req["LoanAmount"] / 1000
    )  # as input loan amount we divided by 1000 wihile training the model
    credit_history = loan_req["Credit_History"]

    input_data = [
        [gender, marital_status, applicant_income, loan_amount, credit_history]
    ]

    prediction = clf.predict(input_data)

    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"Loan approval status:- ": pred}


@app.route("/get_params", methods=["GET"])
def get_params():
    parameters = {
        "Gender": "Male",
        "Married": "Unmarried",
        "ApplicantIncome": 40000,
        "Credit_History": 1.0,
        "LoanAmount": 50000,
    }
    return parameters
