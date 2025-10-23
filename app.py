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
    
    

if __name__ == "__main__":
    main()
