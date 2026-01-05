import streamlit as st
from transcript_loader import load_transcript
from vector_store import create_vector_store
from qa_chain import answer_question

st.set_page_config(page_title="YouTube Video Q&A Bot", layout="centered")

st.title("🎥 YouTube Video Q&A Bot")
st.write("Ask questions about any YouTube video using Retrieval-Augmented Generation (RAG).")

youtube_url = st.text_input("Enter YouTube Video URL")

if youtube_url:
    with st.spinner("Fetching transcript and building knowledge base..."):
        documents = load_transcript(youtube_url)
        vector_store = create_vector_store(documents)

    st.success("Transcript processed successfully!")

    question = st.text_input("Ask a question about the video")

    if question:
        with st.spinner("Finding the answer..."):
            answer = answer_question(vector_store, question)
        st.subheader("Answer")
        st.write(answer)
