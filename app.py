import streamlit as st
import pandas as pd
from main import parse_credit_card_statement
import os

st.title("Credit Card Statement Parser")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())

    
    result = parse_credit_card_statement("temp.pdf")

    
    st.subheader("Extracted Data")
    data = {
        "Field": ["Card Last 4", "Billing Cycle Start", "Billing Cycle End", "Payment Due Date", "Total Balance", "Minimum Payment Due"],
        "Value": [
            result.get("card_last4", "N/A"),
            result.get("billing_cycle", [None, None])[0] if result.get("billing_cycle") else "N/A",
            result.get("billing_cycle", [None, None])[1] if result.get("billing_cycle") else "N/A",
            result.get("payment_due_date", "N/A"),
            result.get("total_balance", "N/A"),
            result.get("min_payment_due", "N/A")
        ]
    }
    df = pd.DataFrame(data)
    st.table(df)

    
    st.subheader("Raw Text Preview")
    st.text(result.get("raw_text_preview", "No preview available"))

    
    os.remove("temp.pdf")
