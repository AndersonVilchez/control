
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Carta de Control (X-bar)")

# Generar datos aleatorios para demostración
st.sidebar.header("Parámetros de los datos")
n_samples = st.sidebar.slider("Número de muestras", min_value=10, max_value=100, value=25)
mean_value = st.sidebar.number_input("Media", value=50.0)
std_dev_value = st.sidebar.number_input("Desviación estándar", value=5.0)

np.random.seed(42)
data = np.random.normal(loc=mean_value, scale=std_dev_value, size=n_samples)
df = pd.DataFrame({
    'Sample': range(1, len(data) + 1),
    'Value': data
})

# Cálculos de control
mean = np.mean(data)
std_dev = np.std(data, ddof=1)
UCL = mean + 3 * std_dev
LCL = mean - 3 * std_dev

# Mostrar datos
st.subheader("Datos generados")
st.write(df)

# Graficar la carta de control
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Sample'], df['Value'], marker='o', linestyle='-', label='Data')
ax.axhline(mean, color='green', linestyle='--', label='Media (Línea central)')
ax.axhline(UCL, color='red', linestyle='--', label='UCL (+3σ)')
ax.axhline(LCL, color='red', linestyle='--', label='LCL (-3σ)')
ax.set_title('Carta de Control (X-bar)')
ax.set_xlabel('Muestra')
ax.set_ylabel('Valor')
ax.legend()
ax.grid(True)

# Mostrar gráfico en Streamlit
st.subheader("Gráfico de Carta de Control")
st.pyplot(fig)
