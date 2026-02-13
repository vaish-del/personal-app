import streamlit as st

st.set_page_config(page_title="Special Message", page_icon="💌")

st.title("Tap the Envelope 💌")

st.write("A little surprise inside...")

# Button click
if st.button("💌 Open Envelope"):
    st.success(
        "Hey Love 💖\n\n"
        "I never really understood what "
        "\"mine\" truly meant...\n\n"
        "until YOU walked into my life.\n\n"
        "And now my world feels warmer, "
        "happier and complete with you.\n\n"
        "I LOVE YOU, MAYUR ❤️"
    )
