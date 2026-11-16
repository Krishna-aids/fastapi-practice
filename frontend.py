import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Insurance Predictor",
    page_icon="🏥",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #888;
    margin-bottom: 30px;
}

.result-card {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
    border: 1px solid rgba(128,128,128,0.3);
}

.result-title {
    font-size: 20px;
    font-weight: 600;
}

.result-value {
    font-size: 42px;
    font-weight: 800;
    margin-top: 10px;
}

.info-card {
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(128,128,128,0.25);
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🏥 Insurance Premium Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered prediction based on your personal and lifestyle information</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("⚙️ About the Model")

    st.write(
        "This application uses a machine-learning model "
        "to predict an insurance premium category."
    )

    st.divider()

    st.subheader("📌 Features Used")

    st.write("• Age")
    st.write("• Weight")
    st.write("• Height")
    st.write("• Income")
    st.write("• Smoking")
    st.write("• City")
    st.write("• Occupation")

    st.divider()

    st.caption("FastAPI Backend: Port 8000")
    st.caption("Streamlit Frontend: Port 8501")


# -----------------------------
# Input Section
# -----------------------------
st.subheader("👤 Enter Your Details")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=119,
        value=30,
        step=1
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=65.0,
        step=0.5
    )

    height = st.number_input(
        "Height (m)",
        min_value=0.5,
        max_value=2.5,
        value=1.70,
        step=0.01
    )

with col2:

    income_lpa = st.number_input(
        "Annual Income (LPA)",
        min_value=0.1,
        max_value=1000.0,
        value=10.0,
        step=0.5
    )

    smoker = st.selectbox(
        "🚬 Are you a smoker?",
        ["No", "Yes"]
    )

    city = st.text_input(
        "📍 City",
        value="Mumbai"
    )

occupation = st.selectbox(
    "💼 Occupation",
    [
        "private_job",
        "government_job",
        "business_owner",
        "freelancer",
        "student",
        "retired",
        "unemployed"
    ]
)


# -----------------------------
# Live BMI
# -----------------------------
if height > 0:

    bmi = weight / (height ** 2)

    st.subheader("📊 Your BMI")

    bmi_col1, bmi_col2 = st.columns([1, 2])

    with bmi_col1:
        st.metric(
            "BMI",
            f"{bmi:.1f}"
        )

    with bmi_col2:

        if bmi < 18.5:
            bmi_status = "Underweight"
        elif bmi < 25:
            bmi_status = "Normal"
        elif bmi < 30:
            bmi_status = "Overweight"
        else:
            bmi_status = "Obese"

        st.info(f"Current status: **{bmi_status}**")


# -----------------------------
# Input Summary
# -----------------------------
with st.expander("🔎 Review Your Information"):

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:
        st.write(f"**Age:** {age}")
        st.write(f"**Weight:** {weight} kg")
        st.write(f"**Height:** {height} m")
        st.write(f"**BMI:** {bmi:.1f}")

    with summary_col2:
        st.write(f"**Income:** ₹{income_lpa} LPA")
        st.write(f"**Smoker:** {smoker}")
        st.write(f"**City:** {city}")
        st.write(f"**Occupation:** {occupation}")


# -----------------------------
# Buttons
# -----------------------------
col_predict, col_reset = st.columns(2)

with col_predict:

    predict_button = st.button(
        "🔮 Predict Premium Category",
        use_container_width=True
    )

with col_reset:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True
    )


# -----------------------------
# Reset
# -----------------------------
if reset_button:

    st.rerun()


# -----------------------------
# Prediction
# -----------------------------
if predict_button:

    # Validation
    if not city.strip():

        st.error("⚠️ Please enter your city.")

    elif height <= 0:

        st.error("⚠️ Height must be greater than zero.")

    else:

        input_data = {
            "age": age,
            "weight": weight,
            "height": height,
            "income_lpa": income_lpa,
            "smoker": smoker == "Yes",
            "city": city,
            "occupation": occupation
        }

        try:

            with st.spinner("🤖 AI model is analyzing your information..."):

                response = requests.post(
                    API_URL,
                    json=input_data,
                    timeout=10
                )

            if response.status_code == 200:

                result = response.json()

                prediction = result.get("predicted_category")

                if prediction:

                    # -------------------------
                    # Prediction Result
                    # -------------------------
                    st.divider()

                    st.subheader("🎯 Prediction Result")

                    if prediction.lower() == "low":

                        icon = "🟢"

                    elif prediction.lower() == "medium":

                        icon = "🟡"

                    elif prediction.lower() == "high":

                        icon = "🔴"

                    else:

                        icon = "🔵"

                    st.markdown(
                        f"""
                        <div class="result-card">

                        <div class="result-title">
                        Predicted Insurance Premium Category
                        </div>

                        <div class="result-value">
                        {icon} {prediction}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # -------------------------
                    # Explanation
                    # -------------------------
                    st.subheader("💡 What does this mean?")

                    if prediction.lower() == "low":

                        st.success(
                            "The model predicts a **Low** premium category "
                            "based on the information provided."
                        )

                    elif prediction.lower() == "medium":

                        st.warning(
                            "The model predicts a **Medium** premium category "
                            "based on the information provided."
                        )

                    elif prediction.lower() == "high":

                        st.error(
                            "The model predicts a **High** premium category "
                            "based on the information provided."
                        )

                    else:

                        st.info(
                            f"The model predicted the category **{prediction}**."
                        )

                    # -------------------------
                    # User Profile
                    # -------------------------
                    st.subheader("📋 Prediction Summary")

                    c1, c2, c3 = st.columns(3)

                    with c1:
                        st.metric("Age", age)

                    with c2:
                        st.metric("BMI", f"{bmi:.1f}")

                    with c3:
                        st.metric("Income", f"{income_lpa} LPA")

                else:

                    st.error("⚠️ API returned no prediction.")

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

                st.write(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to FastAPI. "
                "Make sure Uvicorn is running on port 8000."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ FastAPI took too long to respond."
            )

        except Exception as e:

            st.error(
                f"❌ Unexpected error: {e}"
            )