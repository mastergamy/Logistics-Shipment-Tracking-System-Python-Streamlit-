import streamlit as slt

tracking = slt.Page("tracking.py", title="Tracking", icon="🔎")
data_update = slt.Page("data_update.py", title="Update Data", icon="✔")

pg = slt.navigation([tracking, data_update])

pg.run()