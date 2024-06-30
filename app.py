from flask import Flask, request, jsonify
import numpy as np
import pickle
from sklearn.preprocessing import RobustScaler

app = Flask(__name__)

# Load the trained model and label encoders
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('label_encoders.pkl', 'rb') as file:
    label_encoders = pickle.load(file)

# Load the robust scaler
with open('Robustscaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Endpoint to predict attrition
@app.route('/predict', methods=['POST'])
def predict_attrition():
    data = request.get_json()

    # Extract input values
    Age = data['Age']
    BusinessTravel = data['BusinessTravel']
    DailyRate = data['DailyRate']
    Department = data['Department']
    DistanceFromHome = data['DistanceFromHome']
    Education = data['Education']
    EducationField = data['EducationField']
    EnvironmentSatisfaction = data['EnvironmentSatisfaction']
    Gender = data['Gender']
    HourlyRate = data['HourlyRate']
    JobInvolvement = data['JobInvolvement']
    JobLevel = data['JobLevel']
    JobRole = data['JobRole']
    JobSatisfaction = data['JobSatisfaction']
    MaritalStatus = data['MaritalStatus']
    MonthlyIncome = data['MonthlyIncome']
    MonthlyRate = data['MonthlyRate']
    NumCompaniesWorked = data['NumCompaniesWorked']
    OverTime = data['OverTime']
    PercentSalaryHike = data['PercentSalaryHike']
    PerformanceRating = data['PerformanceRating']
    RelationshipSatisfaction = data['RelationshipSatisfaction']
    StockOptionLevel = data['StockOptionLevel']
    TotalWorkingYears = data['TotalWorkingYears']
    TrainingTimesLastYear = data['TrainingTimesLastYear']
    WorkLifeBalance = data['WorkLifeBalance']
    YearsAtCompany = data['YearsAtCompany']
    YearsInCurrentRole = data['YearsInCurrentRole']
    YearsSinceLastPromotion = data['YearsSinceLastPromotion']
    YearsWithCurrManager = data['YearsWithCurrManager']

    # Collect the features into a dictionary
    feature_dict = {
        'Age': Age,
        'BusinessTravel': BusinessTravel,
        'DailyRate': DailyRate,
        'Department': Department,
        'DistanceFromHome': DistanceFromHome,
        'Education': Education,
        'EducationField': EducationField,
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'Gender': Gender,
        'HourlyRate': HourlyRate,
        'JobInvolvement': JobInvolvement,
        'JobLevel': JobLevel,
        'JobRole': JobRole,
        'JobSatisfaction': JobSatisfaction,
        'MaritalStatus': MaritalStatus,
        'MonthlyIncome': MonthlyIncome,
        'MonthlyRate': MonthlyRate,
        'NumCompaniesWorked': NumCompaniesWorked,
        'OverTime': OverTime,
        'PercentSalaryHike': PercentSalaryHike,
        'PerformanceRating': PerformanceRating,
        'RelationshipSatisfaction': RelationshipSatisfaction,
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': TotalWorkingYears,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': WorkLifeBalance,
        'YearsAtCompany': YearsAtCompany,
        'YearsInCurrentRole': YearsInCurrentRole,
        'YearsSinceLastPromotion': YearsSinceLastPromotion,
        'YearsWithCurrManager': YearsWithCurrManager
    }

    # Encode categorical features using the label encoders
    categorical_columns = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
    for column in categorical_columns:
        feature_dict[column] = label_encoders[column].transform([feature_dict[column]])[0]

    # Convert the dictionary into a numpy array
    features = np.array([[feature_dict[col] for col in feature_dict]])

    # Apply RobustScaler transformation
    scaled_features = scaler.transform(features)

    # Convert scaled_features to a regular Python list for JSON serialization
    scaled_features_list = scaled_features.tolist()

    # Make a prediction
    prediction = model.predict(scaled_features).reshape(1, -1)
    predicted_attrition = int(prediction[0])
   
   
   # Prepare the response
    result = {
        'predicted_attrition': predicted_attrition
    }

    return jsonify(result)

if __name__ == '__main__':
   app.run(debug=True)
