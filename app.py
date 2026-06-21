import streamlit as st
import pandas as pd
import joblib


def load_css():

    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


### ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================
# LOAD MODEL
# ==============================


load_css()


st.markdown(
    """
<div class="hero-box">

<div class="hero-title">
Employee Attrition Intelligence Platform
</div>

<div class="hero-subtitle">
AI Powered Workforce Retention Analytics Dashboard
</div>

</div>
""",
    unsafe_allow_html=True,
)


try:
    model = joblib.load("model.joblib")
except Exception as e:
    st.error(f"Model load failed: {e}")
    st.stop()


# ==============================
# SIDEBAR
# ==============================

st.sidebar.success("✅ Model Loaded")

page = st.sidebar.radio("Navigation", ["Prediction", "Analytics", "About Project"])

# ===================================
# PREDICTION PAGE
# ===================================

if page == "Prediction":
    st.header("Employee Attrition Prediction")

    # YAHAN TUMHARA SAARA INPUT FORM
    # age
    # monthly_income
    # prediction button
    # prediction result

# ===================================
# ANALYTICS PAGE
# ===================================

elif page == "Analytics":
    st.header("Analytics Dashboard")

    st.info("Analytics module under development")

    st.metric("Features", "47")
    st.metric("Model", "Logistic Regression")

# ===================================
# ABOUT PAGE
# ===================================

elif page == "About Project":
    st.header("About Project")

    st.markdown("""
    ### Employee Attrition Prediction System

    This project predicts whether an employee
    is likely to leave the company.

    **Dataset:** IBM HR Analytics

    **Model:** Logistic Regression

    **Developer:** Apoorv Srivastava 

    **Institute:** MNNIT Prayagraj
    """)
# ==============================
# DASHBOARD CARDS
# ==============================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Model", "Logistic Regression")

with c2:
    st.metric("Features", "47")

with c3:
    st.metric("Dataset", "IBM HR")

with c4:
    st.metric("Status", "Live")

st.divider()

# ==============================
# EMPLOYEE INFORMATION
# ==============================

# ==============================
# EMPLOYEE INFORMATION
# ==============================

st.subheader("👨 Employee Information")

with st.expander("👤 Personal Information", expanded=True):
    age = st.slider("Age", 18, 60, 35)

    distance_from_home = st.slider("Distance From Home", 1, 30, 9)

    education = st.slider("Education Level", 1, 5, 3)

with st.expander("💼 Job Information", expanded=True):
    job_role = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources",
        ],
    )

    overtime = st.selectbox("Overtime Status", ["Yes", "No"])

    job_level = st.slider("Job Level", 1, 5, 2)

    job_involvement = st.slider("Job Involvement", 1, 4, 3)

with st.expander("💰 Compensation", expanded=True):
    monthly_income = st.number_input(
        "Monthly Income ($)", min_value=1000, value=5000, step=500
    )

    daily_rate = st.number_input("Daily Rate", min_value=100, value=800)

    hourly_rate = st.slider("Hourly Rate", 10, 100, 65)

    monthly_rate = st.number_input("Monthly Rate", min_value=1000, value=14000)

    percent_salary_hike = st.slider("Salary Hike %", 0, 30, 14)

    stock_option_level = st.slider("Stock Option Level", 0, 3, 1)

with st.expander("📈 Experience", expanded=True):
    total_working_years = st.slider("Total Working Years", 0, 40, 10)

    num_companies_worked = st.slider("Number of Companies Worked", 0, 10, 2)

    years_at_company = st.slider("Years At Company", 0, 40, 5)

    years_in_current_role = st.slider("Years In Current Role", 0, 20, 3)

    years_since_last_promotion = st.slider("Years Since Last Promotion", 0, 15, 1)

    years_with_curr_manager = st.slider("Years With Current Manager", 0, 20, 3)

with st.expander("😊 Satisfaction Metrics", expanded=True):
    environment_satisfaction = st.slider("Environment Satisfaction", 1, 4, 3)

    job_satisfaction = st.slider("Job Satisfaction", 1, 4, 3)

    relationship_satisfaction = st.slider("Relationship Satisfaction", 1, 4, 3)

    work_life_balance = st.slider("Work Life Balance", 1, 4, 3)

with st.expander("🎯 Performance Metrics", expanded=True):
    performance_rating = st.slider("Performance Rating", 1, 4, 3)

    training_times_last_year = st.slider("Training Sessions Last Year", 0, 10, 2)

st.divider()


# ==============================
# INPUT DATAFRAME
# ==============================

base_data = {
    "Age": age,
    "MonthlyIncome": monthly_income,
    "TotalWorkingYears": total_working_years,
    "Overtime": overtime,
    "JobRole": job_role,
    "BusinessTravel": "Travel_Rarely",
    "DailyRate": 800,
    "Department": "Research & Development",
    "DistanceFromHome": 9,
    "Education": 3,
    "EducationField": "Life Sciences",
    "EnvironmentSatisfaction": 3,
    "Gender": "Male",
    "HourlyRate": 65,
    "JobInvolvement": 3,
    "JobLevel": 2,
    "JobSatisfaction": 3,
    "MaritalStatus": "Married",
    "MonthlyRate": 14000,
    "NumCompaniesWorked": 2,
    "PercentSalaryHike": 14,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 3,
    "StockOptionLevel": 1,
    "TrainingTimesLastYear": 2,
    "WorkLifeBalance": 3,
    "YearsAtCompany": 5,
    "YearsInCurrentRole": 3,
    "YearsSinceLastPromotion": 1,
    "YearsWithCurrManager": 3,
}

# Create all 47 features expected by model

input_data = {col: 0 for col in model.feature_names_in_}

# ==============================
# NUMERICAL FEATURES FROM USER
# ==============================

input_data["Age"] = age
input_data["MonthlyIncome"] = monthly_income
input_data["TotalWorkingYears"] = total_working_years

input_data["DailyRate"] = daily_rate
input_data["DistanceFromHome"] = distance_from_home
input_data["Education"] = education
input_data["EnvironmentSatisfaction"] = environment_satisfaction
input_data["HourlyRate"] = hourly_rate
input_data["JobInvolvement"] = job_involvement
input_data["JobLevel"] = job_level
input_data["JobSatisfaction"] = job_satisfaction
input_data["MonthlyRate"] = monthly_rate
input_data["NumCompaniesWorked"] = num_companies_worked
input_data["PercentSalaryHike"] = percent_salary_hike
input_data["PerformanceRating"] = performance_rating
input_data["RelationshipSatisfaction"] = relationship_satisfaction
input_data["StockOptionLevel"] = stock_option_level
input_data["TrainingTimesLastYear"] = training_times_last_year
input_data["WorkLifeBalance"] = work_life_balance
input_data["YearsAtCompany"] = years_at_company
input_data["YearsInCurrentRole"] = years_in_current_role
input_data["YearsSinceLastPromotion"] = years_since_last_promotion
input_data["YearsWithCurrManager"] = years_with_curr_manager
# Constant columns
input_data["EmployeeCount"] = 1
input_data["EmployeeNumber"] = 1
input_data["StandardHours"] = 80

# Overtime
if overtime == "Yes":
    input_data["OverTime_Yes"] = 1

# Business Travel
input_data["BusinessTravel_Travel_Rarely"] = 1

# Department
input_data["Department_Research & Development"] = 1

# Education Field
input_data["EducationField_Life Sciences"] = 1

# Gender
input_data["Gender_Male"] = 1

# Marital Status
input_data["MaritalStatus_Married"] = 1

# Job Role Encoding
job_map = {
    "Human Resources": "JobRole_Human Resources",
    "Laboratory Technician": "JobRole_Laboratory Technician",
    "Manager": "JobRole_Manager",
    "Manufacturing Director": "JobRole_Manufacturing Director",
    "Research Director": "JobRole_Research Director",
    "Research Scientist": "JobRole_Research Scientist",
    "Sales Executive": "JobRole_Sales Executive",
    "Sales Representative": "JobRole_Sales Representative",
}

if job_role in job_map:
    input_data[job_map[job_role]] = 1

input_df = pd.DataFrame([input_data])


st.divider()

predict = st.button("🚀 Predict Employee Attrition", use_container_width=True)

if predict:
    try:
        probabilities = model.predict_proba(input_df)[0]

        stay_probability = probabilities[0] * 100
        leave_probability = probabilities[1] * 100

        prob = probabilities[1]

        st.subheader("📈 Prediction Result")

        # Debug (optional)
        st.write("Leave Probability =", f"{leave_probability:.2f}%")

        # Threshold Based Prediction
        if prob >= 0.30:
            st.markdown(
                """
                <div class="result-danger">
                ⚠️ HIGH ATTRITION RISK
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.markdown(
                """
                <div class="result-success">
                ✅ EMPLOYEE LIKELY TO STAY
                </div>
                """,
                unsafe_allow_html=True,
            )

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Stay Probability", f"{stay_probability:.2f}%")

        with col2:
            st.metric("Leave Probability", f"{leave_probability:.2f}%")

        confidence = max(stay_probability, leave_probability)

        if confidence >= 80:
            st.success("🟢 High Confidence Prediction")

        elif confidence >= 60:
            st.warning("🟡 Moderate Confidence Prediction")

        else:
            st.error("🔴 Low Confidence Prediction")

        st.progress(confidence / 100)

    except Exception as e:
        st.error(f"Prediction Error: {e}")
