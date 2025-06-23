# app.py
import streamlit as st

def main():
    st.title("Welcome App")
    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")

if __name__ == "__main__":
    main()
