import os
import joblib
import pandas as pd
import streamlit as st


# ------------------------------------------------------------
# PAGE
# ------------------------------------------------------------

st.set_page_config(
    page_title="Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)


# ------------------------------------------------------------
# PATHS
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "random_forest_fraud_model.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "models",
    "feature_names.pkl"
)


# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------

@st.cache_resource
def load_files():

    model = joblib.load(MODEL_PATH)
    feature_names = joblib.load(FEATURE_PATH)

    return model, list(feature_names)


try:

    model, feature_names = load_files()

except Exception as e:

    st.error(f"Could not load model: {e}")
    st.stop()


# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("🛡️ FraudGuard AI")

st.write(
    "Credit Card Fraud Detection using Random Forest"
)

st.divider()


# ------------------------------------------------------------
# MODEL INFORMATION
# ------------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "Random Forest")

with col2:
    st.metric("Features", len(feature_names))

with col3:
    st.metric("Precision", "90.59%")

with col4:
    st.metric("F1 Score", "84.15%")


st.divider()


# ------------------------------------------------------------
# TRANSACTION INPUT
# ------------------------------------------------------------

st.header("💳 Transaction Details")


col1, col2 = st.columns(2)

with col1:

    time_value = st.number_input(
        "Transaction Time",
        value=0.0
    )

with col2:

    amount_value = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0
    )


st.subheader("Transaction Features")

st.write(
    "Enter the V1–V28 values used by the trained model."
)


# ------------------------------------------------------------
# V1 - V28
# ------------------------------------------------------------

feature_inputs = {}

columns = st.columns(4)

for i in range(1, 29):

    feature = f"V{i}"

    with columns[(i - 1) % 4]:

        feature_inputs[feature] = st.number_input(
            feature,
            value=0.0,
            format="%.6f"
        )


st.divider()


# ------------------------------------------------------------
# ANALYZE
# ------------------------------------------------------------

if st.button(
    "🔍 Analyze Transaction",
    type="primary"
):

    # --------------------------------------------------------
    # CREATE INPUT VALUES
    # --------------------------------------------------------

    input_values = []

    for feature in feature_names:

        if feature == "Time":

            value = time_value

        elif feature == "Amount":

            value = amount_value

        elif feature.startswith("V"):

            value = feature_inputs[feature]

        elif feature == "Time_hours":

            value = time_value / 3600

        else:

            value = 0.0

        input_values.append(value)


    # --------------------------------------------------------
    # CREATE DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame(
        [input_values],
        columns=feature_names
    )


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    prediction = int(
        model.predict(input_data)[0]
    )

    probability = float(
        model.predict_proba(input_data)[0][1]
    )


    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    st.divider()

    st.header("📊 Prediction Result")


    if prediction == 1:

        st.error(
            "🚨 FRAUD DETECTED"
        )

    else:

        st.success(
            "✅ TRANSACTION IS LEGITIMATE"
        )


    # --------------------------------------------------------
    # PROBABILITY
    # --------------------------------------------------------

    st.subheader("Fraud Probability")

    st.progress(probability)

    st.write(
        f"**{probability * 100:.2f}%**"
    )


    # --------------------------------------------------------
    # DETAILS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Prediction",
            "FRAUD" if prediction == 1 else "LEGITIMATE"
        )

    with col2:

        st.metric(
            "Fraud Probability",
            f"{probability * 100:.2f}%"
        )

    with col3:

        st.metric(
            "Amount",
            f"${amount_value:,.2f}"
        )


    # --------------------------------------------------------
    # INPUT DATA
    # --------------------------------------------------------

    with st.expander("View Input Features"):

        st.dataframe(
            input_data
        )