import streamlit as st
import pandas as pd
import joblib
model = joblib.load("model.pkl")  


st.title("🧬 Gallstone Prediction App")
st.markdown("Enter patient details to predict risk of gallstones.")

# Sidebar inputs
age = st.sidebar.slider("Age", 18, 90, 45)
bmi = st.sidebar.slider("BMI", 10.0, 50.0, 24.5)
hdl = st.sidebar.slider("HDL Cholesterol", 20.0, 100.0, 50.0)
triglycerides = st.sidebar.slider("Triglycerides", 40.0, 800.0, 150.0)
glucose = st.sidebar.slider("Glucose", 70.0, 200.0, 100.0)
crp = st.sidebar.slider("CRP", 0.1, 30.0, 5.0)

# Build input frame
input_df = pd.DataFrame({
    "Age": [age],
    "Body Mass Index (BMI)": [bmi],
    "High Density Lipoprotein (HDL)": [hdl],
    "Triglyceride": [triglycerides],
    "Glucose": [glucose],
    "C-Reactive Protein (CRP)": [crp]
})

# Predict and show result
if st.button("Predict"):
    prob = model.predict_proba(input_df)[0][1]
    threshold = 0.35
    pred = int(prob >= threshold)

    st.write(f"**Gallstone Probability:** {prob:.2f}")
    if pred == 1:
        st.error("⚠️ High Risk of Gallstones")
    else:
        st.success("✅ Low Risk of Gallstones")

# Show entered data
with st.expander("📋 View Patient Data"):
    st.dataframe(input_df)