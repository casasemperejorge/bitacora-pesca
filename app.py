import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración para que se vea bien en móviles
st.set_page_config(page_title="App de Pesca", page_icon="🎣")

# Título con estilo
st.markdown("<h1 style='text-align: center;'>🚢 Bitácora del Capitán</h1>", unsafe_allow_html=True)

# Menú de navegación sencillo
menu = ["Registrar", "Estadísticas"]
choice = st.sidebar.selectbox("Menú", menu)

if choice == "Registrar":
    st.subheader("📝 Nueva Captura")
    
    # Formulario
    with st.form("form_pesca"):
        especie = st.selectbox("Especie", ["Calamar", "Sepia", "Lubina", "Dorada", "Sargo", "Otro"])
        cebo = st.selectbox("Cebo/Cucharilla", ["Potera Roja", "Potera Verde", "Cucharilla Plata", "Rapala", "Vivo"])
        profundidad = st.number_input("Profundidad (metros)", min_value=0, step=1)
        comentarios = st.text_area("Notas (marea, viento, etc.)")
        
        # El componente de cámara
        foto = st.camera_input("Haz una foto a la pieza")
        
        submit = st.form_submit_button("GUARDAR EN BITÁCORA")
        
        if submit:
            # Aquí guardaremos los datos
            st.success(f"¡{especie} guardada! (Falta conectar con el Excel)")
            st.balloons()

elif choice == "Estadísticas":
    st.subheader("📊 Análisis de Pesca")
    st.write("Aquí verás los gráficos cuando conectemos la base de datos.")
