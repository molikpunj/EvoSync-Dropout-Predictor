import streamlit as st
import pandas as pd
import pickle

# --- Load model (adjust path if needed) ---
with open("dropout_model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Page config ---
st.set_page_config(page_title="Student Dropout Predictor", page_icon="🎓", layout="wide")

# --- CSS: gradient + transparency + counselling box styles ---
st.markdown(
    """
    <style>
    /* Apply gradient to body and several app containers (covers many Streamlit versions) */
    body, .stApp, div[data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #071A52 0%, #0f172a 35%, #0f766e 100%) fixed !important;
        background-size: cover !important;
    }

    /* Make the main block container transparent so gradient is visible */
    div[data-testid="stAppViewContainer"] > .main,
    .stApp > .main,
    section.main,
    .block-container {
        background: transparent !important;
    }

    /* Sidebar slightly translucent so it reads well on the gradient */
    [data-testid="stSidebar"] {
        background: rgba(2,6,23,0.55) !important;
        color: #e6f7ff !important;
    }

    /* Header / top toolbar transparency */
    [data-testid="stHeader"], [data-testid="stToolbar"], header {
        background: transparent !important;
    }

    /* Ensure text across the app remains readable on the dark gradient */
    h1, h2, h3, h4, h5, p, label, .stMarkdown, .css-1v0mbdj {
        color: #e6f7ff !important;
    }

    /* Counselling card styles */
    .counsel-box {
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        box-shadow: 0 6px 18px rgba(2,6,23,0.55);
        font-size: 15px;
        line-height: 1.6;
        border: 1px solid rgba(255,255,255,0.03);
    }
    .counsel-risk { background-color: rgba(30,58,95,0.92); color: #ffffff; }
    .counsel-safe { background-color: rgba(6,78,59,0.9); color: #d1fae5; }

    /* Risk label colors */
    .risk-safe { color: #86efac; font-weight: 700; }
    .risk-danger { color: #ff8a8a; font-weight: 700; }

    /* Make metrics and captions readable */
    .stMetric, .stCaption { color: #e6f7ff !important; }

    /* If any Streamlit auto-card has a background, nudge it transparent */
    .stCard, .st-block, .css-18e3th9 { background: transparent !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- App content ---
st.title("🎓 AI-Based Student Dropout Prediction & Counselling")
st.markdown("Upload a CSV file with student details to predict **dropout risks** and generate **counselling suggestions.**")

uploaded_file = st.file_uploader("📂 Upload CSV (Name, Enrollment, Phone, Course, years_in_degree, cgpa, attendance, fee_defaults, leave_apps)", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Could not read CSV: {e}")
        st.stop()

    data.columns = data.columns.str.lower()

    required_cols = {"name", "enrollment", "phone", "course", "years_in_degree", "cgpa", "attendance", "fee_defaults", "leave_apps"}
    if not required_cols.issubset(set(data.columns)):
        st.error("CSV missing required columns. Required: " + ", ".join(sorted(required_cols)))
        st.stop()

    # Extract displayed info and features
    student_info = data[["name", "enrollment", "phone", "course"]].copy()
    features = data[["years_in_degree", "cgpa", "attendance", "fee_defaults", "leave_apps"]]

    # Predictions
    predictions = model.predict(features)
    probs = model.predict_proba(features)[:, 1]

    student_info["Dropout Risk"] = ["At Risk" if p == 1 else "Safe" for p in predictions]
    student_info["Probability (%)"] = [round(float(p) * 100, 2) for p in probs]

    # Summary row
    st.subheader("📊 Prediction Results")
    safe_count = sum(student_info["Dropout Risk"] == "Safe")
    risk_count = sum(student_info["Dropout Risk"] == "At Risk")
    st.markdown(f"**Overview:** {risk_count} At Risk • {safe_count} Safe")

    # Display each student as a row with columns
    for i, row in student_info.iterrows():
        col1, col2, col3, col4 = st.columns([2.5, 1, 1, 1])
        with col1:
            st.write(f"👤 **{row['name']}**  ({row['course']})")
            st.caption(f"Enrollment: {row['enrollment']}  |  Phone: {row['phone']}")
        with col2:
            risk_style = "risk-danger" if row["Dropout Risk"] == "At Risk" else "risk-safe"
            st.markdown(f"<p class='{risk_style}' style='margin:0'>{row['Dropout Risk']}</p>", unsafe_allow_html=True)
        with col3:
            st.metric("Probability", f"{row['Probability (%)']}%")
        with col4:
            # progress requires int 0-100
            try:
                st.progress(int(row["Probability (%)"]))
            except Exception:
                st.progress(0)

    # Counselling messages
    st.subheader("📩 Counselling Messages")
    for i, row in student_info.iterrows():
        if row["Dropout Risk"] == "At Risk":
            st.markdown(f"""
                <div class="counsel-box counsel-risk">
                    <b>Message to {row['name']} ({row['phone']}):</b><br>
                    Hello {row['name']}, we noticed some academic challenges.<br>
                    Would you like to schedule a counselling session?<br>
                    Please reply <b>YES</b> to confirm.
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="counsel-box counsel-safe">
                    <b>Message to {row['name']} ({row['phone']}):</b><br>
                    Great job {row['name']}! 🎉 Keep up the good work.<br>
                    Stay consistent with your studies and attendance.<br>
                    We’re here to support you anytime you need guidance.
                </div>
                """, unsafe_allow_html=True)
