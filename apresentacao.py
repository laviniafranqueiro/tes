import streamlit as st
import pandas as pd

st.title('avaliação do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('jupyter2.csv')  # Assuming 'jupyter2.txt' is your file name

for i in range(df.shape[0]):
    marca = df.iloc[i]['marca']
    preco = df.iloc[i]['preço']
    link = df.iloc[i]['link']
    st.markdown(f"**Marca**: {marca}  \n**Preço**: {preco}  \n**[Link para o produto]({link})**")
