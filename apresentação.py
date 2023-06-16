import streamlit as st
import pandas as pd

st.title('Notebooks e produtos relacionados')
st.caption('Lavínia Franqueiro')

user_input = st.text_input("Qual produto você deseja?")

df = pd.read_csv('jupyter2.csv')  
#defir uma função para converter valores 
def converter_valor(valor):
    valor_limpo = valor.replace('R$,', '').replace('.', '').replace(',', '.')
    return float(valor_limpo)

#Aplicar a função a coluna 'preço'
df['preço2'] = df['preço'].apply(converter_valor)

df = df.sort_values(by='preço2')


# Check if user has entered something in the text input box
if user_input:
    # Filter the DataFrame based on the user input
    df = df[df['marca'].str.contains(user_input, case=False)]

for i in range(df.shape[0]):
    marca = df.iloc[i]['marca']
    preco = df.iloc[i]['preço2']
    link = df.iloc[i]['link']
    st.markdown(f"**Marca**: {marca}  \n**Preço**: {preco}  \n**[Link para o produto]({link})**")
