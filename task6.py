
import streamlit as st

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="Pranasya's Calorie Calculator",
    page_icon="🍎",
    layout="centered"
)

# ---------------------------------------
# Title
# ---------------------------------------
st.title("🍎 Pranasya's Calorie Calculator")

st.write(
    "Enter your personal and activity details to estimate "
    "your daily calorie requirement."
)

st.divider()

# ---------------------------------------
# Personal Details
# ---------------------------------------
st.subheader("👤 Personal Details")

name = st.text_input(
    "Name",
    placeholder="Enter your name"
)

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20,
    step=1
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

# ---------------------------------------
# Body Measurements
# ---------------------------------------
st.subheader("📏 Body Measurements")

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=300.0,
    value=60.0,
    step=0.5
)

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=250.0,
    value=170.0,
    step=0.5
)

# ---------------------------------------
# Activity Level
# ---------------------------------------
st.subheader("🏃 Activity Level")

activity_options = {
    "Sedentary - Little or no exercise": 1.2,
    "Lightly Active - Exercise 1-3 days/week": 1.375,
    "Moderately Active - Exercise 3-5 days/week": 1.55,
    "Very Active - Exercise 6-7 days/week": 1.725,
    "Extra Active - Very hard exercise/physical job": 1.9
}

activity = st.selectbox(
    "Choose your activity level",
    list(activity_options.keys())
)

activity_factor = activity_options[activity]

st.divider()

# ---------------------------------------
# Calculate Calories
# ---------------------------------------
if st.button(
    "🔥 Calculate Calories",
    use_container_width=True
):

    # Check name
    if name.strip() == "":
        st.warning("⚠️ Please enter your name.")

    else:

        # ---------------------------------------
        # Mifflin-St Jeor Equation
        # ---------------------------------------
        if gender == "Male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

        # Total Daily Energy Expenditure
        daily_calories = bmr * activity_factor

        # ---------------------------------------
        # Display Result
        # ---------------------------------------
        st.success("✅ Calculation completed!")

        st.divider()

        st.subheader("📊 Your Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "BMR",
                f"{bmr:.0f} kcal/day"
            )

        with col2:
            st.metric(
                "Estimated Daily Calories",
                f"{daily_calories:.0f} kcal/day"
            )

        # ---------------------------------------
        # Interpretation
        # ---------------------------------------
        st.subheader("💡 Simple Interpretation")

        st.info(
            f"Hi {name}! Based on the information you entered, "
            f"your estimated daily calorie requirement is "
            f"approximately **{daily_calories:.0f} kcal per day** "
            f"to maintain your current weight at your selected "
            f"activity level."
        )

        st.write(
            "Your BMR represents the approximate energy your body "
            "uses at rest. Your estimated daily calorie requirement "
            "also accounts for your selected activity level."
        )

        st.warning(
            "⚠️ This is only an estimate. Actual calorie needs can "
            "vary depending on many factors. For personalized "
            "nutrition advice, consult a qualified healthcare or "
            "nutrition professional."
        )

# ---------------------------------------
# Footer
# ---------------------------------------
st.divider()

st.caption(
    "🍎 Pranasya's Calorie Calculator | "
    "Built with Python + Streamlit"
)