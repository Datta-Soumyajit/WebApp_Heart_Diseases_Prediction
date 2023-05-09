import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
model = data["model"]
le_cpt = data["le_cpt"]
le_ecg = data["le_ecg"]
le_eia = data["le_eia"]
le_fbs = data["le_fbs"]
le_sex = data["le_sex"]
le_slope = data["le_slope"]
le_thal = data["le_thal"]
le_vcf = data["le_vcf"]

def show_predict_page():
    st.title("Heart Disease Prediction")

    st.write("""### We need some information to predict heart disease""")
    
    age = st.slider("Age", 0, 120, 18)
    
    Gender = ("Male", "Female")
    
    sex = st.selectbox("Gender", Gender)
    sex = le_sex.transform([sex])
    
    cpt = ('Typical angina', 'Atypical angina', 'Non-anginal pain')
    
    chest_pain_type = st.selectbox("Chest Pain Type", cpt)
    chest_pain_type = le_cpt.transform([chest_pain_type])
    
    resting_blood_pressure = st.slider("Resting Blood Pressure",60,370,120 )
    
    cholestoral = st.slider("Cholestoral",100,600,200)
    
    fbs = ('Lower than 120 mg/ml', 'Greater than 120 mg/ml')
    
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar", fbs)
    fasting_blood_sugar = le_fbs.transform([fasting_blood_sugar])
    
    
    re = ('ST-T wave abnormality', 'Normal', 'Left ventricular hypertrophy')
    
    rest_ecg = st.selectbox("Rest ECG", re)
    rest_ecg = le_ecg.transform([rest_ecg])
    
    max_heart_rate = st.slider("Maximum Heart Rate",50,220,72 )
    
    eia = ('No', 'Yes')
    
    exercise_induced_angina = st.selectbox("Exercise Induced Angina", eia)
    exercise_induced_angina = le_eia.transform([exercise_induced_angina])
    
    oldpeak = st.number_input(label="Old Peak", step=(0.01), format=("%.2f"))
    
    
    slp = ('Downsloping', 'Upsloping', 'Flat')
    
    slope = st.selectbox("Slope", slp)
    slope = le_slope.transform([slope])
    
    vcf = ('Two', 'Zero', 'One', 'Three', 'Four')
    
    vessels_colored_by_flourosopy = st.selectbox("Vessels Colored by Flourosopy", vcf)
    vessels_colored_by_flourosopy = le_vcf.transform([vessels_colored_by_flourosopy])
    
    
    thal = ('Reversable Defect','Fixed Defect','Normal','No')
    
    thalassemia = st.selectbox("Thalassemia", thal)
    thalassemia = le_thal.transform([thalassemia])
    
    
    
    
    ok = st.button("Predict Heart Disease")
    if ok:
        x = np.array([[age, sex, chest_pain_type, resting_blood_pressure,cholestoral,fasting_blood_sugar, rest_ecg, max_heart_rate, exercise_induced_angina, oldpeak, slope, vessels_colored_by_flourosopy, thalassemia]])
        x = x.astype(float)
        result = model.predict(x)
        if result == [0]:
           st.subheader("Heart Disease Detected")
           
        else:
           st.subheader("Heart Disease Not Detected")