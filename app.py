import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir dispersión') # crear un botón

build_histogram = st.checkbox('Construir un histograma')
build_disp = st.checkbox('Construir una dispersión')
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if disp_button:
        st.write('Creación de grafico de dispersión para el conjunto de datos de anuncios de venta de coches')
        fig = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig, use_container_width=True)


if build_histogram:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        fig = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig, use_container_width=True)

if build_disp:
        st.write('Creación de grafico de dispersión para el conjunto de datos de anuncios de venta de coches')
        fig = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig, use_container_width=True)