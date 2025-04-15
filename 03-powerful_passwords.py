import streamlit as st
import random
import string

# Title of the app
st.title("Powerful Password Generator")

# Input for password length
password_length = st.number_input("Enter the desired password length:", min_value=1, max_value=100, value=12)

# Checkbox options for including characters
include_uppercase = st.checkbox("Include uppercase letters")
include_lowercase = st.checkbox("Include lowercase letters")
include_numbers = st.checkbox("Include numbers")
include_special = st.checkbox("Include special characters")

# Generate password button
if st.button("Generate Password"):
    # Create a pool of characters based on user selection
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Ensure at least one character type is selected
    if characters:
        password = ''.join(random.choice(characters) for _ in range(password_length))
        st.success(f"Generated Password: {password}")
    else:
        st.error("Please select at least one character type to include in the password.")
