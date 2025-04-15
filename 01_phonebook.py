import streamlit as st

# Title of the app
st.title("Phonebook")

# Initialize an empty dictionary to store contacts
if 'phonebook' not in st.session_state:
    st.session_state.phonebook = {}

# Input fields for name and phone number
name = st.text_input("Enter name:")
phone_number = st.text_input("Enter phone number:")

# Button to add contact
if st.button("Add Contact"):
    if name and phone_number:
        st.session_state.phonebook[name] = phone_number
        st.success(f"Contact {name} added!")
    else:
        st.error("Please enter both name and phone number.")

# Display the phonebook
if st.session_state.phonebook:
    st.write("### Phonebook:")
    for name, number in st.session_state.phonebook.items():
        st.write(f"{name}: {number}")
