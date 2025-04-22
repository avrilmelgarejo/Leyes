import streamlit as st

st.set_page_config(page_title="Calculadora de Leyes de Gases", layout="centered")

st.title("Calculadora de Leyes de Gases")
st.write("Selecciona una variable para calcularla usando la Ley combinada de los gases:")
st.latex(r"\frac{P_1 \cdot V_1}{T_1} = \frac{P_2 \cdot V_2}{T_2}")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión final (P2)", "Volumen final (V2)", "Temperatura final (T2)",
     "Presión inicial (P1)", "Volumen inicial (V1)", "Temperatura inicial (T1)")
)

st.subheader("Ingresa los datos conocidos")

# Recolección dinámica de datos
def get_input(label):
    return st.number_input(label, min_value=0.001, format="%.3f")

# Operaciones según la opción seleccionada
if opcion == "Presión final (P2)":
    P1 = get_input("Presión inicial (P1) en atm")
    V1 = get_input("Volumen inicial (V1) en L")
    T1 = get_input("Temperatura inicial (T1) en K")
    V2 = get_input("Volumen final (V2) en L")
    T2 = get_input("Temperatura final (T2) en K")
    if st.button("Calcular P2"):
        P2 = (P1 * V1 * T2) / (T1 * V2)
        st.success(f"La presión final (P2) es: {P2:.3f} atm")
        st.info("Fórmula usada: P2 = (P1 × V1 × T2) / (T1 × V2)")

elif opcion == "Volumen final (V2)":
    P1 = get_input("Presión inicial (P1) en atm")
    V1 = get_input("Volumen inicial (V1) en L")
    T1 = get_input("Temperatura inicial (T1) en K")
    P2 = get_input("Presión final (P2) en atm")
    T2 = get_input("Temperatura final (T2) en K")
    if st.button("Calcular V2"):
        V2 = (P1 * V1 * T2) / (T1 * P2)
        st.success(f"El volumen final (V2) es: {V2:.3f} L")
        st.info("Fórmula usada: V2 = (P1 × V1 × T2) / (T1 × P2)")

elif opcion == "Temperatura final (T2)":
    P1 = get_input("Presión inicial (P1) en atm")
    V1 = get_input("Volumen inicial (V1) en L")
    T1 = get_input("Temperatura inicial (T1) en K")
    P2 = get_input("Presión final (P2) en atm")
    V2 = get_input("Volumen final (V2) en L")
    if st.button("Calcular T2"):
        T2 = (T1 * P2 * V2) / (P1 * V1)
        st.success(f"La temperatura final (T2) es: {T2:.3f} K")
        st.info("Fórmula usada: T2 = (T1 × P2 × V2) / (P1 × V1)")

elif opcion == "Presión inicial (P1)":
    P2 = get_input("Presión final (P2) en atm")
    V2 = get_input("Volumen final (V2) en L")
    T2 = get_input("Temperatura final (T2) en K")
    V1 = get_input("Volumen inicial (V1) en L")
    T1 = get_input("Temperatura inicial (T1) en K")
    if st.button("Calcular P1"):
        P1 = (P2 * V2 * T1) / (T2 * V1)
        st.success(f"La presión inicial (P1) es: {P1:.3f} atm")
        st.info("Fórmula usada: P1 = (P2 × V2 × T1) / (T2 × V1)")

elif opcion == "Volumen inicial (V1)":
    P2 = get_input("Presión final (P2) en atm")
    V2 = get_input("Volumen final (V2) en L")
    T2 = get_input("Temperatura final (T2) en K")
    P1 = get_input("Presión inicial (P1) en atm")
    T1 = get_input("Temperatura inicial (T1) en K")
    if st.button("Calcular V1"):
        V1 = (P2 * V2 * T1) / (T2 * P1)
        st.success(f"El volumen inicial (V1) es: {V1:.3f} L")
        st.info("Fórmula usada: V1 = (P2 × V2 × T1) / (T2 × P1)")

elif opcion == "Temperatura inicial (T1)":
    P2 = get_input("Presión final (P2) en atm")
    V2 = get_input("Volumen final (V2) en L")
    T2 = get_input("Temperatura final (T2) en K")
    P1 = get_input("Presión inicial (P1) en atm")
    V1 = get_input("Volumen inicial (V1) en L")
    if st.button("Calcular T1"):
        T1 = (T2 * P1 * V1) / (P2 * V2)
        st.success(f"La temperatura inicial (T1) es: {T1:.3f} K")
        st.info("Fórmula usada: T1 = (T2 × P1 × V1) / (P2 × V2)")
st.image("1.png")
