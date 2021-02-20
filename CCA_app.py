# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:22:25 2021

@author: shubham mishra
"""

import os
import streamlit as st
import numpy as np
import pickle


os.chdir(r'C:\Users\shubham mishra\Downloads')
model=pickle.load(open('model.pkl','rb'))
def predict_CCA(Age,Debt,EducationLevel,YearsEmployed,PriorDefault,Employed,CreditScore,Income):
    input=np.array([[Age,Debt,EducationLevel,YearsEmployed,PriorDefault,Employed,CreditScore,Income]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)
    
def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Forest Fire Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Age = st.sidebar.slider('Age', 0.00, 100.00, 1.00)
    
    Debt = st.sidebar.slider('Debt', 0.00, 100.00, 1.00)
    
    EducationLevel = st.sidebar.slider('EducationLevel', 1.00, 20.00, 1.00)
    
    YearsEmployed = st.sidebar.slider('YearsEmployed',1.00,60.00,0.00)
    
    PriorDefault = st.sidebar.slider('PriorDefault', 0.00, 1.00, 0.00)
    
    Employed = st.sidebar.slider('Employed', 0.00, 1.00)
    
    CreditScore = st.sidebar.slider('CreditScore', 1.00, 100.00, 1.00)
    
    Income = st.sidebar.slider('Income', 0.00, 100000.00, 1.00)

    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> credit card rejected</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> credit card approved</h2>
       </div>
    """

    if st.button("Predict"):
        output = predict_CCA(Age,Debt,EducationLevel,YearsEmployed,PriorDefault,Employed,CreditScore,Income)
        st.success('The probability of Credit card approval {}'.format(output))

        if output==1:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()