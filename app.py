import streamlit as st

st.title("Iris Flower Predictor")

# --- CREATE THE SIDEBAR INPUTS ---
st.sidebar.header("Input Flower Features")

sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.4)
petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 1.3)
petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)

# --- SHOW THE DATA ON MAIN PAGE ---
st.write("### Current Input Values:")
st.write(f"Sepal: {sepal_length} x {sepal_width} | Petal: {petal_length} x {petal_width}")

# Add your prediction logic below this line...
