import streamlit as st
import pandas as pd

# Datos iniciales
comidas = {
    "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    "Desayuno": [
        "Yogur + granola",
        "Pan integral con queso y huevo + jugo de naranja",
        "Chocolate con cereal",
        "Yogur + granola",
        "Pan integral con queso y huevo + jugo de naranja",
        "Chocolate con cereal",
        "Chocolate con cereal"
    ],
    "Almuerzo": [
        "Arroz con atún, queso y huevo",
        "Pollo a la crema con espinaca",
        "Bife a la criolla con papas",
        "Tacos de pollo",
        "Sandwich integral",
        "Tarta de acelga con huevo",
        "Empanadas de carne y queso"
    ],
    "Cena": [
        "Sorrentinos con crema",
        "Arroz con queso y huevo",
        "Tortilla de papa",
        "Tacos de pollo",
        "Pizza casera",
        "Tarta de choclo",
        "Calabaza rellena"
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
        "Proteínas": ["Pollo", "Atún", "Carne molida", "Huevos", "Queso", "Jamón"],
        "Verduras": ["Espinaca", "Acelga", "Morrón Rojo", "Morrón Verde", "Tomate", "Zanahoria", "Cebolla"],
        "Carbohidratos": ["Arroz", "Pan integral", "Polenta", "Papa"],
        "Extras": ["Crema de leche", "Jugo de naranja", "Lentejas", "Yogur", "Salsa", "Choclo"]
    }
    st.subheader("📌 Lista de Compra")
    for categoria, items in ingredientes.items():
        st.write(f"**{categoria}**: " + ", ".join(items))
