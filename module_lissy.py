import streamlit as st

def render():
    st.header("✨ ليسي - مساعدك الشخصي")
    st.write("---")
    
    # التحقق من وجود ملاحظات في الذاكرة
    if "notes" not in st.session_state:
        st.session_state.notes = []
    
    if len(st.session_state.notes) == 0:
        st.info("لا توجد ملاحظات حتى الآن. اطلب من 'تيدي' تحليل شيء ما!")
    else:
        for i, note in enumerate(st.session_state.notes):
            st.success(f"📝 {note}")
            
    if st.button("مسح جميع الملاحظات"):
        st.session_state.notes = []
        st.rerun()