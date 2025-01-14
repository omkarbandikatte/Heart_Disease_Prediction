import streamlit as st
import pandas as pd
import pickle
import joblib

# Load the trained model
try:
    with open(r"C:\Users\omkar\OneDrive\Desktop\PythonProjects\Machine Learning Projects\new_model.pkl", "rb") as f:
        best_model = pickle.load(f)
except Exception as e:
    st.write(f"Error loading model: {e}")
    st.stop()
# Main function
def main():
    st.title("Heart Disease Prediction")

    # Collect user inputs
    age = st.number_input("Age", min_value=0, max_value=100, value=25)
    sex = st.radio("Sex", ("Male", "Female"))
    cp = st.radio("Feeling Chest Pain", ("Yes", "No"))
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ('Yes', 'No'))
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Low", "Medium", "High"])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
    exang = st.radio("Exercise-Induced Angina", ('Yes', 'No'))
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    slope = st.number_input("The Slope of the Peak Exercise ST Segment", min_value=0, max_value=2, value=1)
    ca = st.number_input("Number of Major Vessels (0-3) Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
    thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversable Defect"])

    # Create input DataFrame
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [1 if sex == "Male" else 0],
        'cp': [1 if cp == "Yes" else 0],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [1 if fbs == "Yes" else 0],
        'restecg': [0 if restecg == "Low" else 1 if restecg == "Medium" else 2],
        'thalach': [thalach],
        'exang': [1 if exang == "Yes" else 0],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [0 if thal == "Normal" else 1 if thal == "Fixed Defect" else 2],
    })

    st.write("Input Data")
    st.write(input_data)

    # Predict button
    if st.button("Predict"):
        try:
            # Make prediction
            result = best_model.predict(input_data)[0]
            if result == 1:
                st.success("Prediction: Heart Disease Detected")
            else:
                st.success("Prediction: No Heart Disease Detected")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == '__main__':
    main()
