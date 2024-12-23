import streamlit as st

st.title("🎈 Mi nueva app ñ")
st.write(
    "Prueba, ¡pruebita funcional! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
cantidad=st.slider('Selecciona la cantidad')

st.write(f'La cantidad seleccionada es: {cantidad}')

for i in range(cantidad):
    st.button(f'{i}')