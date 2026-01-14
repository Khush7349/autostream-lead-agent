from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
def build_vectorstore(path: str = "data/autostream_knowledge.md"):
    loader = TextLoader(path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore
def get_rag_answer(vectorstore, query: str, llm):
    if isinstance(query, dict):
        query = query.get("content", "")
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])
    prompt = f"""
You are an assistant for AutoStream.
Use ONLY the context below to answer the user question.
If the answer is not in the context, say you are not sure.
Context:
{context}
Question:
{query}
Answer:
"""
    response = llm.invoke(prompt)
    return response.content