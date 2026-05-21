import streamlit as st
def render():
    st.header("🤖 تيدي - خبيرك المالي")
    q = st.text_input("أدخل التحليل:")
    if st.button("ترحيل لـ ليسي"):
        st.session_state.notes.append(q)
        st.balloons()