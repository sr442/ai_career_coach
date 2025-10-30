import streamlit as st

st.set_page_config(page_title="AI Career Coach", page_icon="🎯", layout="wide")
st.write("✅ Streamlit launched successfully! If you see this, your UI is working.")
from models.embeddings import RAGEmbedder
from models.llm import query_groq
from utils.rag_utils import extract_text_from_pdf, chunk_text
from utils.web_search import web_search
from utils.response_modes import generate_response

st.set_page_config(page_title="AI Career Coach", page_icon="🎯", layout="wide")
st.title("🎯 AI Career Coach – Smart Career Guidance Powered by Groq")

st.sidebar.header("⚙️ Settings")
mode = st.sidebar.radio("Response Mode", ["Concise", "Detailed"])
source = st.sidebar.radio("Knowledge Source", ["Auto", "RAG", "Web Search"])

uploaded_file = st.sidebar.file_uploader("📄 Upload Career Docs (Resume / PDFs)", type=["pdf"])
embedder = RAGEmbedder()

if uploaded_file:
    with st.spinner("Reading and embedding document..."):
        text = extract_text_from_pdf(uploaded_file)
        chunks = chunk_text(text)
        embedder.create_index(chunks)
    st.sidebar.success("✅ Document processed successfully!")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your AI Career Coach...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("💭 Thinking..."):
            if source == "RAG" and embedder.index:
                context = " ".join(embedder.retrieve(user_input))
                prompt = f"Use this context to answer: {context}\n\nUser: {user_input}"
                response = query_groq(prompt)

            elif source == "Web Search":
                web_data = web_search(user_input)
                prompt = f"Use this information to answer: {web_data}\n\nUser: {user_input}"
                response = query_groq(prompt)

            else:  # Auto mode
                if embedder.index:
                    context = " ".join(embedder.retrieve(user_input))
                    if context.strip():
                        prompt = f"Based on this context, answer: {context}\n\nUser: {user_input}"
                        response = query_groq(prompt)
                    else:
                        web_data = web_search(user_input)
                        response = query_groq(f"Info: {web_data}\nUser: {user_input}")
                else:
                    web_data = web_search(user_input)
                    response = query_groq(f"Info: {web_data}\nUser: {user_input}")

            final_response = generate_response(mode, response)
            st.markdown(final_response)
            st.session_state["messages"].append({"role": "assistant", "content": final_response})

