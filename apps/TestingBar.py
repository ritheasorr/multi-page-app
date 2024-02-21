import streamlit as st
import pandas as pd
from sklearn import datasets



def app():
    st.title('Iris Dataset Summary Page')

    st.write("This is the `New` page of the multi-page app.")

    st.write("The following is the DataFrame Summary of the `iris` dataset.")

    iris = datasets.load_iris()

    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    st.write("Sepal Length vs Sepal Width")

    # Create a bar chart using Streamlit
    st.bar_chart(df[['sepal length (cm)']])


    st.bar_chart(df[['sepal width (cm)']])

    st.write(df.describe())


