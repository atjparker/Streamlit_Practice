# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:25:30 2026

@author: atjpa
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("My First Streamlit App")
st.write("Hello world")

x = st.slider("Pick a number", 0, 100, 50)
st.write("You picked:", x)

if "count" not in st.session_state:
    st.session_state.count = 0
    
if st.button("Increment"):
    st.session_state.count += 1
    
st.write(st.session_state.count)

y = st.selectbox("Pick one", ["A", "B", "C"])


st.write(y)
st.text("text")
st.markdown("**bold**")

df = np.array([1,2,3])
st.dataframe(df)

st.checkbox("Check me")

col1, col2 = st.columns(2)
with col1:
    st.write("Left")
with col2:
    st.write("Right")
    
x = np.linspace(0,10,100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# Calc Practice
with st.sidebar:
    with st.form("Spring_Inputs"):
        F_Spring_K = st.number_input("Front Spring Stiffness (N/mm)")
        R_Spring_K = st.number_input("Rear Spring Stiffness (N/mm)")
        Spring_K = np.array([F_Spring_K, R_Spring_K])
        
        F_Force = st.number_input("Front Force (N)")
        R_Force = st.number_input("Rear Force (N)")
        Force = np.array([F_Force, R_Force])
        submitted = st.form_submit_button("Calculate")
        
@st.cache_data
def run_calc(Spring_K, Force):
    return Force / Spring_K        

if submitted:
    results = run_calc(Spring_K, Force)
    st.write("Front Spring Displacement =", results[0], "mm")
    st.write("Rear Spring Displacement =", results[1], "mm")
