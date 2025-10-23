import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")

def main():
    st.title("Simple Counter App")
    name = st.text_input("Enter your name:", "Guest")
    if st.button("Greet Me"):
        st.write(f"Hello, {name}!")

if __name__ == "__main__":
    main()
    