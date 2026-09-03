import streamlit as st


def show_metrics(total_docs, best_score, search_time):

    st.markdown("### 📊 Search Performance")

    col1, col2, col3 = st.columns(3)

    # =====================================================
    # DOCUMENTS
    # =====================================================

    with col1:

        st.metric(
            label="📄 Documents",
            value=f"{total_docs:,}",
            help="Total documents available in the knowledge base."
        )

    # =====================================================
    # BEST MATCH
    # =====================================================

    with col2:

        st.metric(
            label="🎯 Best Match",
            value=f"{best_score:.1f}%",
            help="Similarity score of the highest-ranked document."
        )

    # =====================================================
    # SEARCH TIME
    # =====================================================

    with col3:

        st.metric(
            label="⚡ Search Time",
            value=f"{search_time} ms",
            help="Time taken to retrieve the search results."
        )