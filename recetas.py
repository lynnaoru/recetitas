import streamlit as st
import pandas as pd

# Datos iniciales
comidas = {
    "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    "Desayuno": [
        "Yogur + avena + semillas de calabaza",
        "Pan integral con queso + jugo de naranja",
        "Huevos revueltos con espinaca",
        "Smoothie de banana y espinaca",
        "Tostadas con palta y huevo",
        "Yogur con granola",
        "Pan con mantequilla de maní"
    ],
    "Almuerzo": [
        "Arroz con atún, queso y espinaca",
        "Pollo a la crema con hígado",
        "Bife a la criolla con papas",
        "Tacos de pollo",
        "Pizza casera",
        "Tarta de acelga",
        "Empanadas de carne"
    ],
    "Cena": [
        "Sopa de lentejas",
        "Revuelto de espinaca",
        "Polenta con salsa de carne",
        "Tortilla de papa",
        "Pan con atún",
        "Calabaza rellena",
        "Sándwich de pollo"
    ]
}

df_comidas = pd.DataFrame(comidas)

# Interfaz
st.title("🍽️ Planificador de Comiditas")
st.write("Personaliza el menú semanal y genera la lista de compras.")

# Mostrar/editar tabla
st.subheader("📅 Menú Semanal")
edited_df = st.data_editor(df_comidas, num_rows="dynamic")

# Generar lista de compras
if st.button("🛒 Generar Lista de Compra"):
    ingredientes = {
        "Proteínas": ["Pollo", "Atún", "Carne molida", "Hígado", "Huevos", "Queso"],
        "Verduras": ["Espinaca", "Acelga", "Morrón", "Tomate", "Zanahoria", "Repollo"],
        "Carbohidratos": ["Arroz", "Pan integral", "Polenta", "Papa"],
        "Extras": ["Semillas de calabaza", "Jugo de naranja", "Lentejas", "Yogur"]
    }
    st.subheader("📌 Lista de Compra")
    for categoria, items in ingredientes.items():
        st.write(f"**{categoria}**: " + ", ".join(items))
