import streamlit as st
import module_markets, module_teddy, module_lissy, module_news

st.set_page_config(layout="wide", page_title="SmartBlink OS")

if "page" not in st.session_state: st.session_state.page = "home"
if "notes" not in st.session_state: st.session_state.notes = []

st.title("🚀 SmartBlink AI ● النظام المالي المتكامل")
c1, c2, c3, c4 = st.columns(4)

if c1.button("📊 الأسواق"): st.session_state.page = "markets"
if c2.button("🤖 تيدي"): st.session_state.page = "teddy"
if c3.button("✨ ليسي"): st.session_state.page = "lissy"
if c4.button("📰 الأخبار"): st.session_state.page = "news"

if st.session_state.page == "markets": module_markets.render()
elif st.session_state.page == "teddy": module_teddy.render()
elif st.session_state.page == "lissy": module_lissy.render()
elif st.session_state.page == "news": module_news.render()