# ============================================
# MÓDULO 4 · EQUIPO DE TRABAJO
# ============================================

st.header("👥 Equipo de trabajo")

equipo = [
    {
        "nombre": "Dra. Elena Elsa Bricio Barrios",
        "rol": "Coordinadora académica del proyecto",
        "detalle": "Especialista en Psicología Educativa y Vocacional"
    },
    {
        "nombre": "Dr. Santiago Arceo-Díaz",
        "rol": "Desarrollo metodológico y análisis de datos",
        "detalle": "Doctor en Ciencias Médicas, con experiencia en modelos predictivos"
    },
    {
        "nombre": "Psic. Martha Cecilia Ramírez Guzmán",
        "rol": "Aplicación y validación en campo",
        "detalle": "Psicóloga con experiencia en orientación vocacional"
    }
]

cols = st.columns(len(equipo))

for col, integrante in zip(cols, equipo):
    with col:
        st.markdown(
            f"""
            <div style="
                border:1px solid #ddd;
                border-radius:12px;
                padding:18px;
                background-color:#f9fafb;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
                ">
                <h4 style="margin-bottom:5px;">{integrante['nombre']}</h4>
                <p style="margin:0; color:#2563eb; font-weight:bold;">{integrante['rol']}</p>
                <p style="margin-top:6px; font-size:0.9em; color:#4b5563;">{integrante['detalle']}</p>
            </div>
            """, unsafe_allow_html=True
        )
