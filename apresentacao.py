import streamlit as st
import pandas as pd

st.title('avaliação do Josir')
st.caption('Lavínia Franqueiro')

user_input = st.text_input("Digite a marca do notebook que você está procurando:")

df = pd.read_csv('jupyter2.csv')  # Assuming 'jupyter2.txt' is your file name

# Check if user has entered something in the text input box
if user_input:
    # Filter the DataFrame based on the user input
    df = df[df['marca'].str.contains(user_input, case=False)]

for i in range(df.shape[0]):
    marca = df.iloc[i]['marca']
    preco = df.iloc[i]['preço']
    link = df.iloc[i]['link']
    st.markdown(f"**Marca**: {marca}  \n**Preço**: {preco}  \n**[Link para o produto]({link})**")
