import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="OLA Ride Insights Dashboard",
    layout="wide"
)

# Title
st.title("🚖 OLA Ride Insights Dashboard")

# Load Data
try:
    df = pd.read_csv("ola_rides.csv")
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

# Clean Column Names
df.columns = df.columns.str.strip()

# KPIs
total_bookings = len(df)

if "Booking_Value" in df.columns:
    total_revenue = df["Booking_Value"].sum()
else:
    total_revenue = 0

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Bookings", f"{total_bookings:,}")

with col2:
    st.metric("Total Revenue", f"₹{total_revenue:,.0f}")

st.markdown("---")

# Booking Status
if "Booking_Status" in df.columns:
    st.subheader("Booking Status Distribution")

    fig1 = px.pie(
        df,
        names="Booking_Status",
        title="Booking Status"
    )
    st.plotly_chart(fig1, use_container_width=True)

# Vehicle Type
if "Vehicle_Type" in df.columns:
    st.subheader("Vehicle Type Distribution")

    vehicle_counts = df["Vehicle_Type"].value_counts().reset_index()
    vehicle_counts.columns = ["Vehicle_Type", "Count"]

    fig2 = px.bar(
        vehicle_counts,
        x="Vehicle_Type",
        y="Count",
        title="Vehicle Type Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Payment Method
if "Payment_Method" in df.columns:
    st.subheader("Payment Method Distribution")

    fig3 = px.pie(
        df,
        names="Payment_Method",
        title="Payment Method Distribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

# Revenue by Vehicle Type
if "Vehicle_Type" in df.columns and "Booking_Value" in df.columns:

    st.subheader("Revenue by Vehicle Type")

    revenue = (
        df.groupby("Vehicle_Type")["Booking_Value"]
        .sum()
        .reset_index()
    )

    fig4 = px.bar(
        revenue,
        x="Vehicle_Type",
        y="Booking_Value",
        title="Revenue by Vehicle Type"
    )

    st.plotly_chart(fig4, use_container_width=True)

# Customer Ratings
if "Customer_Rating" in df.columns:

    st.subheader("Customer Rating Distribution")

    fig5 = px.histogram(
        df,
        x="Customer_Rating",
        nbins=10,
        title="Customer Ratings"
    )

    st.plotly_chart(fig5, use_container_width=True)

# Ride Distance
if "Ride_Distance" in df.columns:

    st.subheader("Ride Distance Distribution")

    fig6 = px.histogram(
        df,
        x="Ride_Distance",
        nbins=20,
        title="Ride Distance"
    )

    st.plotly_chart(fig6, use_container_width=True)

# Data Preview
st.subheader("Dataset Preview")
st.dataframe(df.head(20))

st.success("OLA Ride Insights Dashboard Loaded Successfully ✅")