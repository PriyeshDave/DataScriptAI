import streamlit as st

OPENAI_API_KEY = st.secrets['api_keys']["OPENAI_API_KEY"]
MODEL_NAME = "gpt-4-turbo"

TABLE_SCHEMA = {
    "transactions": ["transaction_id", "amount", "timestamp", "merchant_id", "card_number"],
    "cards": ["card_number", "card_type", "cvv", "expiry_date", "account_holder"]
}
