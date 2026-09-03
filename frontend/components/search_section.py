import streamlit as st


def show_search_section():

    # =====================================================
    # SEARCH SECTION
    # =====================================================

    with st.container(border=True):

        # # Search title
        # st.markdown(
        #     """
        #     <div class="search-title">
        #         🔍 Enterprise Knowledge Search
        #     </div>
        #     """,
        #     unsafe_allow_html=True
        # )

        # Description
        st.markdown(
            """
            <div class="search-description">
                Ask questions in natural language.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # Search input
        query = st.text_input(
            "Search",
            placeholder="How do I reset my password?",
            label_visibility="collapsed"
        )

        st.write("")

        # Search button
        search = st.button(
            "🚀 Search",
            use_container_width=True
        )

    return query, search