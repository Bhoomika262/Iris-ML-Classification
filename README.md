# 🌸 Iris Species Classification Using Machine Learning

## Project Overview

This project is a machine learning classification system that predicts the species of an Iris flower based on its sepal and petal measurements.

The project uses the standard Iris dataset available through `sklearn.datasets` and compares multiple machine learning algorithms before selecting the best-performing model.

## Features

- Exploratory Data Analysis (EDA)
- Data preprocessing and feature scaling
- Train-test split with stratification
- Multiple machine learning classification models
- PCA dimensionality reduction
- LDA dimensionality reduction
- Model performance comparison
- Accuracy, Precision, Recall and F1-Score evaluation
- Confusion matrices
- Prediction probability/confidence
- Complete preprocessing and model pipeline
- Model saved using Joblib
- Interactive Streamlit web application

## Dataset

The Iris dataset is loaded using:

`sklearn.datasets.load_iris()`

It contains four input features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The target classes are:

- Setosa
- Versicolor
- Virginica

## Machine Learning Models

The following classification models were implemented and compared:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Naive Bayes

## Dimensionality Reduction

Two dimensionality reduction techniques were explored:

- Principal Component Analysis (PCA)
- Linear Discriminant Analysis (LDA)

Their performance was compared with the original feature space.

## Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The best-performing model was selected based on the actual evaluation results.

## Streamlit Application

The project includes an interactive Streamlit application where users can enter the four Iris flower measurements and receive:

- Predicted flower species
- Prediction confidence/probability for each species

## 🌐 Live Demo

**Streamlit App:**  
https://iris-ml-classification-vcngmucyx9ps6tpdaxv2mr.streamlit.app/

## Project Structure

```text
Iris-ML-Classification/
│
├── app.py
├── iris_model.pkl
├── requirements.txt
└── README.md
```

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/bhoomika262/iris-ml-classification.git
```

Move into the project directory:

```bash
cd iris-ml-classification
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Deployment

The application is deployed using Streamlit Community Cloud and connected to the GitHub repository.

## Future Improvements

- Add more interactive visualizations
- Add hyperparameter tuning
- Improve the user interface
- Add model explainability
- Improve prediction analysis for uncertain inputs
- Extend the project to other classification datasets

## Authors

**Bhoomika**  
**Mansi Sharma**

B.Tech CSE (IoT)  
SKIT Jaipur
