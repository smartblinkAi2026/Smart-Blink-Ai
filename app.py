import streamlit as st

st.set_page_config(layout="wide", page_title="SmartBlink AI")

st.title("🚀 SmartBlink AI ● النظام المالي الموحد")

# إنشاء جلسة لتخزين البيانات
if "notes" not in st.session_state: st.session_state.notes = []

# الأزرار في الأعلى
c1, c2, c3, c4 = st.columns(4)
if c1.button("📊 الأسواق"): st.session_state.page = "markets"
if c2.button("🤖 تيدي"): st.session_state.page = "teddy"
if c3.button("✨ ليسي"): st.session_state.page = "lissy"
if c4.button("📰 الأخبار"): st.session_state.page = "news"

# عرض الصفحات
if st.session_state.get("page") == "markets":
    st.subheader("📊 بوابة الأسواق")
    st.write("الأسهم والعملات الرقمية في مكان واحد.")
    
elif st.session_state.get("page") == "teddy":
    st.subheader("🤖 تيدي - خبيرك المالي")
    q = st.text_input("أدخل تحليل الأسهم:")
    if st.button("ترحيل لـ ليسي"):
        st.session_state.notes.append(q)
        st.balloons()
        st.success("تم الحفظ!")

elif st.session_state.get("page") == "lissy":
    st.subheader("✨ ليسي - مساعدك الشخصي")
    for note in st.session_state.notes:
        st.write(f"📝 {note}")

elif st.session_state.get("page") == "news":
    st.subheader("📰 الأخبار الاقتصادية")
    st.write("📢 ارتفاع الذهب، تقلبات الكريبتو.")
