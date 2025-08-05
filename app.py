# app.py
import streamlit as st
from pdf_reader import extract_text_from_pdf
from embedder import embed_texts, find_most_relevant_chunk

st.set_page_config(page_title="AskMyPDF", layout="wide")

st.title("📄 AskMyPDF")
st.write("Upload a PDF and ask any question about its content.")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# Initialize session state to store embeddings and chunks
if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "embeddings" not in st.session_state:
    st.session_state.embeddings = []

# Process uploaded PDF
if uploaded_file:
    with st.spinner("Reading and embedding your PDF..."):
        st.session_state.chunks = extract_text_from_pdf(uploaded_file)
        st.session_state.embeddings = embed_texts(st.session_state.chunks)
    st.success("PDF processed successfully!")

# Ask a question
if st.session_state.chunks:
    question = st.text_input("Ask a question about the PDF:")
    
    if question:
        with st.spinner("Searching for the best answer..."):
            results = find_most_relevant_chunk(
                question,
                st.session_state.chunks,
                st.session_state.embeddings,
                top_k=1
            )
            answer, score = results[0]
        
        st.subheader("🔎 Best Match")
        st.write(answer)
        st.caption(f"Relevance Score: {score:.2f}")
