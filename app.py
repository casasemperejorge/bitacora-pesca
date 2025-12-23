import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Configuración de página
st.set_page_config(page_title="Bitácora de Pesca", page_icon="🎣")

st.markdown("<h1 style='text-align: center;'>🚢 Bitácora del Capitán</h1>", unsafe_allow_html=True)

# CONEXIÓN A GOOGLE SHEETS
# (Sustituye 'TU_URL_AQUÍ' por la URL de tu Google Sheets más adelante)
url = "https://docs.google.com/spreadsheets/d/1L7oMU_kQQ5sNprA1XAIf5XM7jKNCztzOcW9hdCxonD0/edit?gid=0#gid=0"
conn = st.connection("gsheets", type=GSheetsConnection)

menu = ["Registrar", "Estadísticas"]
choice = st.sidebar.selectbox("Menú", menu)

if choice == "Registrar":
    st.subheader("📝 Nueva Captura")
    
    with st.form("form_pesca"):
        especie = st.selectbox("Especie", ["Calamar", "Sepia", "Lubina", "Dorada", "Sargo", "Otro"])
        cebo = st.selectbox("Cebo/Cucharilla", ["Potera Roja", "Potera Verde", "Cucharilla Plata", "Rapala", "Vivo"])
        profundidad = st.number_input("Profundidad (metros)", min_value=0)
        comentarios = st.text_area("Notas")
        
        submit = st.form_submit_button("GUARDAR EN BITÁCORA")
        
        if submit:
            # Creamos una nueva fila de datos
            nueva_fila = pd.DataFrame([{
                "Fecha": datetime.now().strftime("%d/%m/%Y"),
                "Hora": datetime.now().strftime("%H:%M"),
                "Especie": especie,
                "Cebo": cebo,
                "Profundidad": profundidad,
                "Comentarios": comentarios
            }])
            
            # Leemos los datos actuales y añadimos la nueva fila
            data_existente = conn.read(spreadsheet=url)
            actualizado = pd.concat([data_existente, nueva_fila], ignore_index=True)
            
            # Guardamos de vuelta en Google Sheets
            conn.update(spreadsheet=url, data=actualizado)
            
            st.success("¡Datos guardados en Google Sheets!")
            st.balloons()

elif choice == "Estadísticas":
    st.subheader("📊 Análisis de Pesca")
    df = conn.read(spreadsheet=url)
    if not df.empty:
        st.write("Resumen de capturas:")
        st.bar_chart(df["Especie"].value_counts())
    else:
        st.write("Aún no hay datos para mostrar.")
