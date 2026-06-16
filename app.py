import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🏠 Hostel Energy Consumption Analysis")

uploaded_file = st.file_uploader(
    "Upload Hostel Energy CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df.columns = df.columns.str.strip()

    st.subheader("Dataset")
    st.dataframe(df)

    energy_col = "TOTAL ENERGY CONSUMPTION(UNITS)"

    total_energy = df[energy_col].sum()
    avg_energy = df[energy_col].mean()

    highest_room = df.loc[df[energy_col].idxmax(), "ROOM NO"]
    lowest_room = df.loc[df[energy_col].idxmin(), "ROOM NO"]

    st.subheader("Energy Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Consumption", f"{total_energy:.2f} kWh")
        st.metric("Highest Room", highest_room)

    with col2:
        st.metric("Average Consumption", f"{avg_energy:.2f} kWh")
        st.metric("Lowest Room", lowest_room)

    st.subheader("Room-wise Energy Consumption")

    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(df["ROOM NO"], df[energy_col])
    ax.set_xlabel("Room Number")
    ax.set_ylabel("Energy (kWh)")
    st.pyplot(fig)

    st.subheader("Energy Saving Suggestions")

    st.success("""
    • Switch off fans and lights when not in use.
    • Use LED bulbs.
    • Unplug chargers after charging.
    • Enable laptop power-saving mode.
    • Create awareness among hostel residents.
    """)

else:
    st.info("Please upload a CSV file to start analysis.")