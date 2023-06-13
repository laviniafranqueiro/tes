import streamlit as st
import pandas as pd

st.title('Notebooks e produtos relacionados')
st.caption('Lavínia Franqueiro')

user_input = st.text_input("Qual produto você deseja?")

df = pd.read_csv('jupyter2.csv') 

# Check if user has entered something in the text input box
if user_input:
    # Filter the DataFrame based on the user input
    df = df[df['marca'].str.contains(user_input, case=False)]

# Sort the DataFrame by 'preço' column in ascending order
df = df.sort_values('preço')

for i in range(df.shape[0]):
    marca = df.iloc[i]['marca']
    preco = df.iloc[i]['preço']
    link = df.iloc[i]['link']
    st.markdown(f"*Marca: {marca}  \nPreço: {preco}  \n*[Link para o produto]({link})**")
