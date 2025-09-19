# 🎓 AI-Based Student Dropout Prediction & Counselling System  

## 📌 Overview  
This project is a prototype for the **JIMS Smart India Hackathon 2025** problem statement:  
**AI-Based Dropout Prediction and Counselling System**.  

The system:  
1. Predicts which students are **at risk of dropping out** using their academic and behavioral data.  
2. Displays predictions in a **Streamlit dashboard**.  
3. Simulates **automated counselling messages** via WhatsApp-style prompts.  
4. (Future scope) Allows students to reply and schedule real counselling sessions.  

---

## 🚀 Features  
- 📂 Upload a CSV file with student details.  
- 🧠 ML Model (Logistic Regression) trained on academic data.  
- 📊 Dashboard showing dropout risk and probability for each student.  
- 💬 Auto-generated counselling messages for at-risk students.  
- 🔒 Easy to extend with WhatsApp Business API for real messaging.  

---

## 🛠️ Tech Stack  
- **Python 3.13+**  
- **scikit-learn** → ML model (Logistic Regression)  
- **pandas** → data preprocessing  
- **Streamlit** → interactive dashboard  
- **pickle** → saving/loading trained model  

---

## 📂 Project Structure  
```
├── dropout_model.py       # Script to train and save the ML model
├── app.py                 # Streamlit web app
├── dropout_model.pkl      # Saved ML model (generated after training)
├── sample_students_1.csv    # Example CSV file for testing
└── README.md              # Project documentation
```

---

## ⚡ Setup Instructions  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/molikpunj/EvoSync-Dropout-Predictor.git
cd JIMS-SIH-2025
```

### 2️⃣ Create a virtual environment (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Train the model  
```bash
python dropout_model.py
```

This generates `dropout_model.pkl`.

### 5️⃣ Run the Streamlit app  
```bash
streamlit run app.py
```

---

## 📊 Sample CSV Format  
The CSV file should have these columns:  

```
Name,Enrollment,Phone,Course,years_in_degree,cgpa,attendance,fee_defaults,leave_apps
Arjun Kumar,ENR001,9876543210,BCA,1,7.8,85,0,2
Benny Smith,ENR002,9876501234,BBA,2,6.2,55,1,5
Priya Sharma,ENR003,9876123456,B.Tech,3,5.1,40,1,6
Rohit Verma,ENR004,9876789123,B.Com,4,8.3,92,0,1
```

---

## 📌 Future Scope  
- ✅ Integrate **WhatsApp Business API** for real message sending.  
- ✅ Add **student response handling** (YES/NO to book sessions).  
- ✅ Build a **counsellor dashboard** to manage appointments.  
- ✅ Use deep learning models for higher accuracy.  

---

## 🤝 Team EvoSync – JIMS Smart India Hackathon 2025  
Developed as part of **Problem Statement ID – 25102**  
Theme: Smart Automation 