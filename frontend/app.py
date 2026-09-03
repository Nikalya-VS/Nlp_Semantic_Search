import streamlit as st
import time

from components.styles import load_css
from components.sidebar import show_sidebar
from components.navbar import show_navbar
from components.hero import show_hero
from components.search_section import show_search_section
from components.metrics import show_metrics
from components.result_card import show_result

from services.api_client import search_documents

st.set_page_config(
    page_title="Semantic Search AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

show_sidebar()
load_css()

show_navbar()
show_hero()

query, search = show_search_section()

# ===========================
# SEARCH LOGIC STARTS HERE
# ===========================

if not search:

    st.info(
        "👆 Enter a question above to search your enterprise knowledge base."
    )

if search:

    if query.strip():

        with st.spinner("Searching documents..."):

            start = time.perf_counter()

            response = search_documents(query)

            end = time.perf_counter()

        if "results" in response:

            results = response["results"]

            if results:

                show_metrics(
                    total_docs=50000,
                    best_score=results[0]["similarity"] * 100,
                    search_time=round((end - start) * 1000)
                )
                
                st.write("")
                st.write("")

                st.success(
                    f"Found {len(results)} relevant documents."
                )

                st.divider()

                st.subheader("📄 Search Results")

                st.caption(
                    "Top matching enterprise documents ranked using semantic similarity."
                )

                for result in results:

                    show_result(result)

            else:

                st.warning("No matching documents found.")

        else:

            st.error("Unexpected API response.")

    else:

        st.warning("Please enter a search query.")