import streamlit as st
import pandas as pd
import pickle

with open("dropout_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 AI-Based Student Dropout Prediction & Counselling")

st.write("Upload a CSV file with student details (Name, Enrollment, Phone, Course, Years, CGPA, Attendance, Fee Defaults, Leave Applications).")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    data.columns = data.columns.str.lower()
    
    student_info = data[["name", "enrollment", "phone", "course"]]
    
    features = data[["years_in_degree", "cgpa", "attendance", "fee_defaults", "leave_apps"]]
    
    predictions = model.predict(features)
    probs = model.predict_proba(features)[:, 1]
    
    student_info["Dropout Risk"] = ["At Risk" if p == 1 else "Safe" for p in predictions]
    student_info["Probability"] = [round(p*100, 2) for p in probs]

    st.subheader("📋 Prediction Results")
    st.dataframe(student_info)
    
    st.subheader("📩 Counselling Messages")
    for i, row in student_info.iterrows():
        if row["Dropout Risk"] == "At Risk":
            st.write(f"Message to {row['name']} ({row['phone']}):")
            st.info(f"Hello {row['name']}, we noticed some academic challenges. Would you like to schedule a counselling session? Please reply YES to confirm.")
