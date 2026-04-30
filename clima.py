import streamlit as st
import requests

st.set_page_config(page_title="App del Clima", page_icon="🌦️")

st.title("🌦️ Consulta el Clima")
st.write("Escribe una ciudad para ver el clima actual")

ciudad = st.text_input("Ciudad")

API_KEY = "2e1bddc26a2be40063953e894daf1f5f"

if st.button("Buscar"):

    if ciudad != "":
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

        respuesta = requests.get(url)
        datos = respuesta.json()

        if respuesta.status_code == 200:

            temp = datos["main"]["temp"]
            humedad = datos["main"]["humidity"]
            descripcion = datos["weather"][0]["description"]

            st.success(f"Clima en {ciudad}")
            st.metric("🌡️ Temperatura", f"{temp} °C")
            st.metric("💧 Humedad", f"{humedad}%")
            st.write("☁️ Estado:", descripcion)

        else:
            st.error("Ciudad no encontrada")
    else:
        st.warning("Escribe una ciudad")