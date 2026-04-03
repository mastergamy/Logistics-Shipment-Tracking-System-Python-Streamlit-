import streamlit as slt
import pandas as pd
import os

CN = slt.number_input("Please input Tracking No", placeholder="Tracking No", value=None, step=1, max_value=99999999999)
bkg_date = slt.date_input("Please Input Booking Date", format="DD-MM-YYYY")
origin = slt.text_input("Plesae input Shipment origin").upper()
destination = slt.text_input("Please input Shipmemt Destination").capitalize()
sender = slt.text_input("Please input Customer Name").capitalize()
consignee = slt.text_input("Please input Consignee Name").capitalize()
dly_date = slt.date_input("Please Input Delivery Date", format="DD-MM-YYYY")
rcvd_by = slt.text_input("Please input Receiver Name").capitalize()
status = slt.selectbox("Select Status", ["OK", "NP", "BA", "CN"])

file_loc = "tracking.csv"

if not os.path.exists(file_loc):
    df = pd.DataFrame(columns=[
        "Tracking No","Booking Date","Origin","Destination",
        "Sender Name","Consignee Name","Delivery Date",
        "Received By","Status"
    ])
    df.to_csv(file_loc, index=False)
else:
    df = pd.read_csv(file_loc)

if slt.button("Add data"):

    if not CN: # Checks for empty fields
        slt.error("Tracking number is required")
        slt.stop()
    elif origin == "" or destination == "" or sender=="" or consignee=="" or rcvd_by=="":
        slt.error("Please fill out the empty fields.")
        slt.stop()


    if not df["Tracking No"].isin([CN]).any(): #Checks for CN duplicacy
        new_df = pd.DataFrame({
            "Tracking No" : [CN],
            "Booking Date" : [bkg_date],
            "Origin" : [origin],
            "Destination" : [destination],
            "Sender Name" : [sender],
            "Consignee Name" : [consignee],
            "Delivery Date" : [dly_date],
            "Received By" : [rcvd_by],
            "Status" : [status]
        })

        new_df.to_csv(file_loc, header=False, mode="a", index=False)
        slt.success("Data added succesfully")

    elif df["Status"].isin(["OK"]).any():
        slt.error("You cannot update data, it is already delivered.")

    else:
        same_data = df[df["Tracking No"] == CN].sort_values(by="Delivery Date", ascending=True).iloc[-1].to_dict()
        new_df = pd.DataFrame({
            "Tracking No" : [same_data["Tracking No"]],
            "Booking Date" : [pd.to_datetime(same_data["Booking Date"], errors="coerce")],
            "Origin" : [same_data["Origin"]],
            "Destination" : [same_data["Destination"]],
            "Sender Name" : [same_data["Sender Name"]],
            "Consignee Name" : [same_data["Consignee Name"]],
            "Delivery Date" : [dly_date],
            "Received By" : [rcvd_by],
            "Status" : [status]
        })

        new_df.to_csv(file_loc, header=False, mode="a", index=False)
        slt.success("Data added succesfully")