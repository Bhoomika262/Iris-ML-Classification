
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Iris Species Classifier",
    page_icon="🌸",
    layout="wide"
)

model = joblib.load("iris_model.pkl")

st.title("🌸 Iris Species Classifier")
st.write("Predict the species of an Iris flower using machine learning.")

st.subheader("Enter Flower Measurements")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
    sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)

with col2:
    petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
    petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

if st.button("Predict Species"):
    sample = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)"
        ]
    )

    prediction = model.predict(sample)[0]
    probabilities = model.predict_proba(sample)[0]

    species = ["setosa", "versicolor", "virginica"]

    st.success(f"Predicted Species: {species[prediction]}")

    st.subheader("Prediction Confidence")

    probability_df = pd.DataFrame({
        "Species": species,
        "Probability": probabilities
    })

    st.bar_chart(
        probability_df.set_index("Species")
    )
