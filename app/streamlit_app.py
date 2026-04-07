import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Ecommerce Analysis",
    page_icon="🛒",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------
file_path = os.path.join(os.path.dirname(__file__), "..", "results", "customer_segments.csv")
data = pd.read_csv(file_path)

# ----------------------------
# Title
# ----------------------------
st.title("🛒 Ecommerce Customer Behaviour Dashboard")

st.markdown("### 📊 Analyze customer segments & behavior")

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("🔍 Filters")

cluster = st.sidebar.selectbox(
    "Select Cluster",
    sorted(data['Cluster_KMeans'].unique())
)

# ----------------------------
# Filtered Data
# ----------------------------
filtered = data[data['Cluster_KMeans'] == cluster]

# ----------------------------
# KPI Metrics
# ----------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(filtered))
col2.metric("Avg Spend", round(filtered['AvgSpend'].mean(), 2))
col3.metric("Total Items", int(filtered['TotalItems'].sum()))
col4.metric("Avg Rating", round(filtered['AvgRating'].mean(), 2))

# ----------------------------
# Data Table
# ----------------------------
st.subheader("📄 Customer Data")

st.dataframe(filtered, use_container_width=True)

# ----------------------------
# Charts Section
# ----------------------------
st.subheader("📈 Visual Insights")

col1, col2 = st.columns(2)

# Avg Spend Distribution
with col1:
    fig, ax = plt.subplots()
    sns.histplot(filtered['AvgSpend'], kde=True, ax=ax)
    ax.set_title("Avg Spend Distribution")
    st.pyplot(fig)

# Total Items
with col2:
    fig, ax = plt.subplots()
    sns.boxplot(y=filtered['TotalItems'], ax=ax)
    ax.set_title("Total Items Purchased")
    st.pyplot(fig)

# ----------------------------
# Cluster Comparison
# ----------------------------
st.subheader("📊 Cluster Comparison")

fig, ax = plt.subplots()
sns.barplot(x='Cluster_KMeans', y='AvgSpend', data=data, ax=ax)
ax.set_title("Avg Spend per Cluster")
st.pyplot(fig)

# ----------------------------
# Download Option
# ----------------------------
st.subheader("⬇️ Download Data")

csv = filtered.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_customers.csv",
    mime="text/csv"
)

# ----------------------------
# Recommendations Section
# ----------------------------
st.subheader("🛍️ Recommendations")

st.info("Example product associations:")
st.write("📱 Mobile → 🎧 Earphones")
st.write("💻 Laptop → 🖱️ Mouse")
st.write("👗 Dress → 👠 Heels")