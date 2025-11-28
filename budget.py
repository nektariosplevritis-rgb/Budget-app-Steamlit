# budget.py
import streamlit as st

st.title("Monthly Budget")
st.write("Calculation of income after expenses")

# ---------- INPUTS ----------
st.header("Net salary")
salary = st.number_input("Monthly salary after tax (in €)", min_value=0.0, value=2500.0, step=100.0)

st.write("---")

st.header("Monthly Expenses")
rent           = st.number_input("Rent or mortgage",            min_value=0.0, value=800.0)
utilities      = st.number_input("Electricity + water + internet + mobile", min_value=0.0, value=200.0)
food           = st.number_input("Food & groceries",           min_value=0.0, value=400.0)
transport      = st.number_input("Gas, car repairs, public transport", min_value=0.0, value=150.0)
subscriptions  = st.number_input("Netflix, Spotify, gym, etc.", min_value=0.0, value=60.0)

st.write("---")

# ---------- CALCULATIONS ----------
total_expenses = rent + utilities + food + transport + subscriptions
remaining = salary - total_expenses         # <-- this line was missing!

# ---------- RESULTS ----------
st.header("Result")

col1, col2, col3 = st.columns(3)
col1.metric("Net Salary", f"€{salary:,.0f}")
col2.metric("Total Expenses", f"€{total_expenses:,.0f}")

if remaining >= 0:
    col3.metric("Left for savings/fun", f"€{remaining:,.0f}")
else:
    col3.metric("Shortfall", f"€{remaining:,.0f}", delta="Need to borrow!")

# Progress bar
if salary > 0:
    spent_percent = (total_expenses / salary) * 100
    st.progress(spent_percent / 100)
    st.write(f"You've spent {spent_percent:.1f}% of your salary")

# Messages
if remaining > 500:
    st.balloons()
    st.success("Amazing! You can save or invest")
elif remaining >= 0:
    st.info("You're okay, but maybe cut some subscriptions")
else:
    st.error("Over budget! Time to reduce expenses or earn more")


