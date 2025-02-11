import streamlit as st
import info

st.title("Animales")
st.header(info.nombre_elefante)
columna1, columna2 = st.columns(2)

with columna1:
    # Contenido de la columna 1
    st.image(info.foto_elefante, caption=info.nombre_elefante.title())
with columna2:
    # Contenido de la columna 2
    st.write(f"**Descripción:** {info.descripcion_elefante}")
    pais1, pais2, pais3, pais4 = st.columns(4, vertical_alignment="center")
    with pais1:
      st.image(info.bandera_kenya, caption="Kenya")
    with pais2:
      st.image(info.bandera_tanzania, caption="Tanzania")
    with pais3:
      st.image(info.bandera_zimbabwe, caption="Zimbabwe")
    with pais4:
      st.image(info.bandera_bostwana, caption="Botswana")
    st.map(info.coordenadas_elefante, use_container_width=True, height=300, zoom=0, size=1000000)
