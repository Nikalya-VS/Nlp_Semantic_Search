import streamlit as st


def show_sidebar():

    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    with st.sidebar:

        st.markdown('<div class="sidebar-title">🔍 Semantic Search AI</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="sidebar-subtitle">Enterprise Knowledge Retrieval</div>',
            unsafe_allow_html=True,
        )

        dark = st.toggle(
            "🌙 Dark Mode",
            value=st.session_state.theme == "dark",
        )

        st.session_state.theme = "dark" if dark else "light"

        st.divider()