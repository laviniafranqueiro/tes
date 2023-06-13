import streamlit as st
import pandas as pd 
import csv
st.title('avaliação do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('jupyter2', sep =',')
st.dataframe(df)
