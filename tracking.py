import streamlit as slt
import pandas as pd

df = pd.read_csv("tracking.csv")

tracking_no = slt.number_input("Please Enter Tracking No", value=None, step=1)

filtered_df = df[df["Tracking No"] == tracking_no]

slt.subheader("Tracking Info")
slt.dataframe(filtered_df, hide_index=True)

last_value = filtered_df.sort_values(by="Delivery Date", ascending=True).tail(1)
try:
    if (last_value["Status"] == "OK").item(): # To check whether Shipment is delivered or not
        slt.write("Your shipment is Delivered")
    else:
        attempts = len(filtered_df.index) # To check the number of attempts made
        slt.write(f"Your shipment still remains undelivered after {attempts} attempt(s).")
except:
    slt.write("No Data Found")