import streamlit as st


def show_result(result):

    similarity = result.get("similarity", 0) * 100

    title = result.get("title", "Untitled Document")

    category = result.get(
        "category",
        "Unknown"
    )

    content = result.get(
        "content",
        ""
    )

    keywords = result.get(
        "keywords",
        []
    )

    # =====================================================
    # RESULT CONTAINER
    # =====================================================

    with st.container(border=True):

        # =================================================
        # HEADER
        # =================================================

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(
                f"### 📄 {title}"
            )

            st.caption(
                f"📂 {category}"
            )

        with col2:

            st.metric(
                "Match",
                f"{similarity:.1f}%"
            )

        # =================================================
        # SIMILARITY
        # =================================================

        st.progress(
            min(max(similarity / 100, 0.0), 1.0)
        )

        st.caption(
            f"Semantic similarity: {similarity:.1f}%"
        )

        # =================================================
        # CONTENT PREVIEW
        # =================================================

        preview = content[:250]

        if len(content) > 250:

            preview += "..."

        st.write(preview)

        # =================================================
        # FULL DOCUMENT
        # =================================================

        with st.expander("📄 Read Full Document"):

            st.write(content)

            if keywords:

                st.markdown("**🔑 Keywords**")

                if isinstance(keywords, list):

                    st.write(
                        ", ".join(map(str, keywords))
                    )

                else:

                    st.write(keywords)