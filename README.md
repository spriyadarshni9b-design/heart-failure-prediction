# Heart Failure Prediction

A machine learning project that predicts the risk of mortality in patients with heart failure using clinical data. The project uses a Random Forest Classifier and is deployed as an interactive Streamlit web application.

The model is trained using clinical features such as age, ejection fraction, serum creatinine, serum sodium, and other patient-related measurements. The project also evaluates class imbalance and uses a custom prediction threshold to improve the detection of positive cases.

> **Disclaimer:** This project is developed for educational purposes only and is not intended to provide medical diagnosis or clinical decisions.

## Objectives

- Analyze clinical data related to heart failure.
- Identify important factors associated with patient mortality.
- Build a machine learning model to predict mortality risk.
- Evaluate model performance, particularly for the positive class.
- Deploy the final model as an interactive Streamlit web application.

## Dataset

The project uses the Heart Failure Clinical Records dataset.

The dataset contains **299 patient records** and **13 variables**, including clinical and demographic features such as:

- Age
- Anaemia
- Creatinine phosphokinase
- Diabetes
- Ejection fraction
- High blood pressure
- Platelets
- Serum creatinine
- Serum sodium
- Sex
- Smoking
- Time
- DEATH_EVENT

The target variable is `DEATH_EVENT`, where:

- `0` represents patients who did not die during the follow-up period.
- `1` represents patients who died during the follow-up period.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Google Colab

## Data Preprocessing

The dataset was checked for missing values, duplicate records, and data types before model training.

The target variable `DEATH_EVENT` was separated from the input features. The data was then divided into training and testing sets using an 80:20 split with stratification to preserve the class distribution.

The `time` feature was excluded from the final model because it represents the follow-up period after the patient's clinical assessment and could make the prediction less suitable for estimating risk based only on the available clinical characteristics.

The final model uses the remaining 11 clinical features as input.

## Model Development

Several classification approaches were evaluated during the project to identify a suitable model for predicting the target class.

The final model selected was a **Random Forest Classifier**. The `time` feature was excluded from the final model to avoid relying on the follow-up duration as a prediction input.

The data was split into training and testing sets using an 80:20 stratified split.

## Model Evaluation

The final Random Forest model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Since correctly identifying patients in the positive class was an important objective, the prediction threshold was adjusted from the default `0.50` to `0.25`.

At the selected threshold of `0.25`, the model achieved:

| Metric | Class 0 | Class 1 |
|---|---:|---:|
| Precision | 0.87 | 0.50 |
| Recall | 0.63 | 0.79 |
| F1-score | 0.73 | 0.61 |

**Overall accuracy: 68%**

The selected threshold improved recall for Class 1 to **79%**, meaning the model correctly identified 15 out of 19 positive cases in the test set. This was prioritized over overall accuracy because detecting more positive cases was considered more important for this project.

## Streamlit Application

The trained Random Forest model was deployed using Streamlit to create an interactive web application.

The application allows users to enter the required clinical information and receive a predicted risk based on the trained model.

The application uses the same 11 features used during model training and applies the selected prediction threshold of `0.25`.

### Application Features

- User-friendly input fields
- Clinical feature selection
- Random Forest prediction
- Probability-based risk prediction
- Custom classification threshold
- Interactive web interface

> **Disclaimer:** The application is intended for educational and demonstration purposes only and should not be used for medical diagnosis or treatment decisions.
## Project Structure

```text
heart-failure-prediction/
│
├── app.py
├── heart_failure_model.pkl
├── heart_failure_project.ipynb
├── heart_failure_clinical_records_dataset.csv
└── README.md
