import streamlit as st


def show_navbar():

    col1, col2 = st.columns([7, 3])

    with col1:
        st.markdown(
            """
            <div style="
                display:flex;
                align-items:center;
                gap:12px;
                font-size:24px;
                font-weight:700;
            ">
                <span style="font-size:30px;">🔍</span>
                <span>Semantic Search AI</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="
                text-align:right;
                padding-top:10px;
                font-size:14px;
            ">
                Enterprise Knowledge Retrieval
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()