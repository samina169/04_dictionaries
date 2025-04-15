import streamlit as st

# Title of the app
st.title("Number Counter")

# Input for the user to enter numbers
numbers_input = st.text_input("Enter numbers separated by commas:")

if numbers_input:
    # Split the input string into a list of numbers
    numbers = [int(num) for num in numbers_input.split(",") if num.strip().isdigit()]
    
    # Count the numbers
    count = len(numbers)
    
    # Display the count
    st.write(f"Count of numbers: {count}")
