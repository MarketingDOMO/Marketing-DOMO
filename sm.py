import streamlit as st
import pandas as pd
import altair as alt


def main():
    # Page Setup
    st.set_page_config(
        page_title="Marketing DOMO",
        page_icon="🏂",
        layout="wide",
        initial_sidebar_state="expanded")
    alt.themes.enable("dark")
    # --------------

    tab0, tab1, tab2, tab3 = st.tabs(["Overview", "Social Media", "PR", "Podcast"])

    with tab0:
        st.markdown('ABC')
    with tab1:
        st.markdown('ABC')
    with tab2:
        st.markdown('ABC')
    with tab3:
        st.markdown('ABC')


    # st.title("🎈 My new app")
    # st.write(
    #     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    # )

main()
