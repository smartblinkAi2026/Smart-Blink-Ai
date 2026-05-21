import streamlit as st

def render():
    st.header("📰 أخبار السوق الحية")
    st.write("---")
    
    # قائمة الأخبار
    news_list = [
        "ارتفاع قياسي في أسعار الذهب اليوم",
        "توقعات إيجابية لأسهم شركات التكنولوجيا",
        "العملات الرقمية تشهد تقلبات حادة هذا الأسبوع"
    ]
    
    for news in news_list:
        st.info(f"📢 {news}")
        
    st.warning("تحديث الأخبار يتم كل ساعة تلقائياً.")