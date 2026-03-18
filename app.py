import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# 1. Setup the Page
st.set_page_config(page_title="Iris Predictor", page_icon="🌸")
st.title("Iris Flower Predictor")
st.markdown("---")

# 2. Create the Sidebar for User Inputs
st.sidebar.header("Input Flower Features")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# 3. Display the User Inputs on the Main Page
st.subheader('Selected Input Parameters')
st.write(df)

# 4. The Prediction Logic (Self-contained Model)
iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

# 5. Display the Results
st.subheader('Class Labels and their Index Number')
st.write(iris.target_names)

st.subheader('Prediction')
st.success(f"The predicted species is **{iris.target_names[prediction][0]}**")

st.subheader('Prediction Probability')
st.write(prediction_proba)
