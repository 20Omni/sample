
import streamlit as st
import pandas as pd

st.title("AI Task Management Dashboard")

df = pd.read_csv("final_task_assignment.csv")

st.write("### Final Task Assignment")
st.dataframe(df[['Task ID', 'Priority', 'deadline_days_remaining', 'New Assigned User']])
