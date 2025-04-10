import streamlit as st

def main():
    """Main function that serves as the entry point for the Streamlit application"""
    st.title("My Streamlit Application")
    
    # Add your app components here
    st.write("Welcome to my Streamlit app!")
    
    # Example of adding some interactive elements
    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")
    
    # Example of a button
    if st.button("Click me!"):
        st.write("Button was clicked!")

if __name__ == "__main__":
    main()
