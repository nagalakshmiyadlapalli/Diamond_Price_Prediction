import streamlit as st
import pandas as pd
import pickle

# Load model
with open("diamond_knn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💎 Diamond Price Prediction App")
st.write("Enter diamond details to predict price")

# ---------------- USER INPUTS ----------------
carat = st.number_input("Carat", min_value=0.1, step=0.01)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"]
)

color = st.selectbox(
    "Color",
    ["D", "E", "F", "G", "H", "I", "J"]
)

clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

depth = st.number_input("Depth", min_value=0.0)
table = st.number_input("Table", min_value=0.0)
x = st.number_input("X dimension")
y = st.number_input("Y dimension")
z = st.number_input("Z dimension")

# ---------------- ENCODING (IMPORTANT PART) ----------------

cut_map = {
    "Fair": 0,
    "Good": 1,
    "Very Good": 2,
    "Premium": 3,
    "Ideal": 4
}

color_map = {
    "D": 0,
    "E": 1,
    "F": 2,
    "G": 3,
    "H": 4,
    "I": 5,
    "J": 6
}

clarity_map = {
    "I1": 0,
    "SI2": 1,
    "SI1": 2,
    "VS2": 3,
    "VS1": 4,
    "VVS2": 5,
    "VVS1": 6,
    "IF": 7
}

cut_encoded = cut_map[cut]
color_encoded = color_map[color]
clarity_encoded = clarity_map[clarity]

# ---------------- CREATE INPUT DATAFRAME ----------------
input_data = pd.DataFrame([[carat,cut_encoded,color_encoded,clarity_encoded,depth,table,x,y,z]], 
                          columns=[ "carat", "cut", "color", "clarity", "depth", "table", "x", "y", "z"])

# ---------------- PREDICT ----------------
if st.button("Predict Price 💰"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Diamond Price: 💵 ${prediction[0]:.2f}")