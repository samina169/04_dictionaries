import streamlit as st

# Title of the app
st.title("Pop-Up Shop")

# Sample product data
products = {
    "T-shirt": 20.00,
    "Jeans": 40.00,
    "Hat": 15.00,
    "Sneakers": 60.00
}

# Initialize an empty cart in session state
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Display products
st.write("### Available Products:")
for product, price in products.items():
    st.write(f"{product}: ${price:.2f}")
    if st.button(f"Add {product} to Cart"):
        if product in st.session_state.cart:
            st.session_state.cart[product] += 1
        else:
            st.session_state.cart[product] = 1
        st.success(f"{product} added to cart!")

# Display the cart
if st.session_state.cart:
    st.write("### Your Cart:")
    for product, quantity in st.session_state.cart.items():
        st.write(f"{product}: {quantity} (Total: ${products[product] * quantity:.2f})")
    total_price = sum(products[product] * quantity for product, quantity in st.session_state.cart.items())
    st.write(f"**Total Price: ${total_price:.2f}**")
else:
    st.write("Your cart is empty.")
