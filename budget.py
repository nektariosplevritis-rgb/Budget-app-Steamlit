# budget.py

import streamlit as st

# Page layout
st.title("Monthly Budget")
st.write("Calcualation of income after expenses")

# Salary input
st.header("Net salary")
salary = st.number_input("Monthly salary after tax (in €)", min_value=0.0, value=10000.0)

st.write("---")  # a line to separate sections

# Expenses input
st.header("Expenses")

rent = st.number_input("Rent or mortgage", min_value=0.0, value=1500.0)
utilities = st.number_input("Electricity + water + internet + mobile", min_value=0.0, value=400.0)
food = st.number_input("Food & groceries", min_value=0.0, value=600.0)
transport = st.number_input("gas + car repairs", min_value=0.0, value=300.0)
subscriptions = st.number_input("Netflix, Spotify, gym", min_value=0.0, value=100.0)

# Calculate everything (with print-style comments)
st.write("---")
st.header("Remaining Balance")

expenses = rent + utilities + food + transport + subscriptions
Remaining Balance = Net salary - Expenses

# Column markers
col1, col2, col3 = st.columns(3)
col1.metric("Net salary", f"€{Net salary:,.0f}")
col2.metric("Expenses", f"€{expenses:,.0f}")
if Remaining Balance >= 0:
    col3.metric("Left for extra", f"€{Remaining Balance:,.0f}")
else:
    col3.metric("Left", f"€{Remaining Balance:,.0f}", delta="need to borrow!")

# Progress bar 
percentage_spent = (Expenses / Net Salary) * 100 if salary > 0 else 0
st.progress(percentage_spent / 100)

# Message outputs
if Remaining Balance > 300:
    st.balloons()
    st.success("Nice! I can invest")
elif money_left >= 0:
    st.info("Okay, i need to cut expenses")
else:
    st.error("I need to borrow for the expenses and cut next month..")

