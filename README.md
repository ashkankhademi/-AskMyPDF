# 📄 AskMyPDF

AskMyPDF is a lightweight web app that lets you **upload any PDF** and **ask natural language questions** about its content. It uses **transformer-based sentence embeddings** to understand the meaning of your question and find the most relevant section from the document.

---

## 🧰 Built With

- 🧠 [Sentence-Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
- 📄 PyMuPDF for PDF text extraction
- 🔍 Cosine similarity for semantic search
- 🖥️ Streamlit for the web interface

---

## 🚀 Features

- 📤 Upload any standard PDF  
- 💬 Ask freeform questions like “What’s the refund policy?” or “Where did Ashkan study?”  
- 🧠 Smart matching using vector-based semantic similarity  
- ⚡ Fast, lightweight, and runs locally in seconds

---

## 🛠️ How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/ashkankhademi/AskMyPDF.git
   cd AskMyPDF

2. **Install dependencies**
   ```bash
   pip install streamlit pymupdf sentence-transformers scikit-learn

3. **Run the app**
   ```bash
   streamlit run app.py

