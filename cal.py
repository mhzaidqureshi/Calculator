import streamlit as st

st.title("Calculator")

user1 = st.number_input("write a number")
user2 = st.number_input("write a number1")
option = st.selectbox("Select optoion",["+","-","*","/"])

if option == "+":
    st.success(user1 + user2)
elif option == "-":
    st.success(user1 - user2)
elif option == "*":
    st.success(user1 * user2)
elif option == "/":
    st.success(user1 / user2)
elif user1 == 0 and option == "/":
    st.error("can't divisible by zero")
else:
    st.error("enter a value")