import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Fin-Ops Sentinel Dashboard",
    page_icon="📊",
    layout="centered"
)

st.title("Fin-Ops Sentinel")
st.markdown("AI-powered financial risk monitoring dashboard")

tab1, tab2 = st.tabs(["Fraud Detection", "Sentiment Analysis"])


with tab1:
    st.header("Fraud Detection")

    amount = st.number_input("Amount", min_value=0.0, value=80000.0, step=1000.0)
    transaction_type = st.selectbox(
        "Transaction Type",
        ["cash_out", "transfer", "payment", "debit"]
    )
    old_balance_org = st.number_input("Old Balance", min_value=0.0, value=90000.0, step=1000.0)
    new_balance_org = st.number_input("New Balance", min_value=0.0, value=0.0, step=1000.0)

    if st.button("Check Fraud Risk"):
        payload = {
            "amount": amount,
            "transaction_type": transaction_type,
            "old_balance_org": old_balance_org,
            "new_balance_org": new_balance_org
        }

        try:
            response = requests.post(f"{API_BASE_URL}/predict/fraud", json=payload)
            response.raise_for_status()
            result = response.json()

            st.success("Fraud prediction completed")

            st.subheader("Prediction Result")
            st.write(f"**Fraud Risk:** {result['fraud_risk']}")
            st.write(f"**Fraud Probability:** {result['fraud_probability']}")
            st.write(f"**Reason:** {result['reason']}")

            st.subheader("Risk Factors")
            risk_factors = result.get("risk_factors", {})
            st.write(f"**Amount Risk:** {risk_factors.get('amount_risk', 'N/A')}")
            st.write(f"**Transaction Pattern:** {risk_factors.get('transaction_pattern', 'N/A')}")
            st.write(f"**Model Confidence:** {risk_factors.get('model_confidence', 'N/A')}")

            st.subheader("Raw Response")
            st.json(result)

        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")


with tab2:
    st.header("Financial Sentiment Analysis")

    text = st.text_area(
        "Enter financial or business text",
        value="The company reported strong quarterly growth and improved market confidence."
    )

    if st.button("Analyze Sentiment"):
        payload = {"text": text}

        try:
            response = requests.post(f"{API_BASE_URL}/predict/sentiment", json=payload)
            response.raise_for_status()
            result = response.json()

            st.success("Sentiment analysis completed")

            st.subheader("Prediction Result")
            st.write(f"**Sentiment:** {result['sentiment']}")
            st.write(f"**Confidence:** {result['confidence']}")
            st.write(f"**Source:** {result['source']}")

            st.subheader("Raw Response")
            st.json(result)

        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")