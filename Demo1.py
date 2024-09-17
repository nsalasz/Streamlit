import streamlit as st




st.title('Interactive Slider Example')

slider_value = st.slider('Selecciona un valor:', 0, 100, 50)
st.write(f'Tu seleccion {slider_value}!')



st.title('Interactive Checkbox Example')

checkbox_value = st.checkbox('Check me')
if checkbox_value:
    st.write('Checkbox is checked!')
else:
    st.write('Checkbox is not checked.')



st.title('Entrada de texto interactiva')

user_text = st.text_input('Ingrese su texto:')
st.write(f'Su entrada: {user_text}')







##st.image("./a.jpg")


