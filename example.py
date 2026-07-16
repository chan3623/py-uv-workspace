
import streamlit as st
import pandas as pd


header_list = []
csv = pd.read_csv("source/records.csv")

for i in range(1, 4):
    header_list.append(st.text_input(f"header_{i}"))

if all(header_list):
    csv.columns = header_list
    st.table(csv)
