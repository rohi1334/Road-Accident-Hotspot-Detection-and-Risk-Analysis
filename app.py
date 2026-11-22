import streamlit as st

st.set_page_config(page_title="Road Accident Risk System", layout="wide")

st.title("🚦 Road Accident Hotspot Detection & Analysis System")

st.markdown("""
Welcome to the Road Accident Analysis System.

Use the sidebar to navigate:

- 🗺 Hotspot Map
- 🛣 Route Risk Analysis
- 📊 Dashboard
""")

st.write(
"This system uses historical accident data to identify dangerous zones and help users travel safely."
)

st.success("System Ready ✅")

st.divider()

# Help Button
if st.button("❓ Help / How to Use"):
    st.switch_page("pages/5_Help.py")

st.sidebar.title("Navigation")
st.sidebar.info("Select a page from the sidebar.")