import streamlit as st
st.title("Example")
no=st.text_input("Enter No")
if(st.button("Clickme")):
    if int(no)%2==0:
        st.write("Ans is")
        st.write("No is Even")
        st.balloons()

    else:
        st.write("Ans is")
        st.warning("No is Odd")