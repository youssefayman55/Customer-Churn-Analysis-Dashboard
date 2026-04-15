import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Page Config
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("📊 Customer Churn Analysis Dashboard")
st.markdown("Analyzing customer behavior to understand the causes of churn 🔥")


# Load Data
df = pd.read_csv("Bank_Churn_Classification_Dataset.csv")


# Sidebar Filters
st.sidebar.header("🔍 Filters")
gender = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())
contract = st.sidebar.multiselect("Contract", df["Contract"].unique(), default=df["Contract"].unique())

filtered_df = df[
    (df["Gender"].isin(gender)) &
    (df["Contract"].isin(contract))
]


# KPIs (Metrics)
col1, col2, col3  = st.columns(3)

with col1:
    st.metric("👥 Total Customers", len(filtered_df))

with col2:
    churn_rate = filtered_df["Churn"].mean() * 100
    st.metric("⚠️ Churn Rate %", f"{churn_rate:.2f}%")

with col3:
    avg_monthly = filtered_df["MonthlyCharges"].mean()
    st.metric("💰 Avg Monthly Charges", f"{avg_monthly:.2f}")

st.divider()


# Charts Section
col1, col2 = st.columns(2)


# 1. Churn Distribution
with col1:
    st.subheader("📊 Churn Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x="Churn", data=filtered_df, ax=ax)
    st.pyplot(fig)


# 2. Contract vs Churn
with col2:
    st.subheader("📊 Contract vs Churn")
    fig, ax = plt.subplots()
    sns.countplot(x="Contract", hue="Churn", data=filtered_df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)


# Second Row Charts
col1, col2 = st.columns(2)

# 3. Monthly Charges vs Churn
with col1:
    st.subheader("💰 Monthly Charges vs Churn")
    fig, ax = plt.subplots()
    sns.boxplot(x="Churn", y="MonthlyCharges", data=filtered_df, ax=ax)
    st.pyplot(fig)


# 4. Tenure vs Churn
with col2:
    st.subheader("⏳ Tenure vs Churn")
    fig, ax = plt.subplots()
    sns.boxplot(x="Churn", y="Tenure", data=filtered_df, ax=ax)
    st.pyplot(fig)


# Footer Insights
st.divider()
st.subheader("🧠 Key Insights")

st.write("""
- Customers with short tenure are more likely to churn.
- Monthly contracts show higher churn rates.
- Higher monthly charges may increase churn probability.
""")