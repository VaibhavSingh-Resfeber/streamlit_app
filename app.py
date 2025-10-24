import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")

def main():
    st.title("Simple Counter App")
    name = st.text_input("Enter your name:", "Guest")
    if st.button("Greet Me"):
        st.write(f"Hello, {name}!")


    # Add Chart
    st.subheader("Randome line Chart")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)
    
    # Color picker
    st.subheader("Pick a Color")
    color = st.selectbox("Choose a color:",["Red", "Green", "Blue", "Yellow"])
    if st.button("Show Color"):
        st.write(f"You selected: {color}")
        st.markdown(f"<div style='width:100px; height:100px; background-color:{color.lower()};'></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
