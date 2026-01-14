# AutoStream Lead Agent 🚀  
*A conversational AI sales assistant for a SaaS product*

AutoStream Lead Agent is a Python-based AI chatbot that behaves like a real website assistant for a SaaS startup. It can answer product questions, understand user intent, and guide interested users through a lead-capture flow — just like a real sales bot on a landing page.

This project is built to demonstrate how modern AI agents are designed in production:

- Intent detection  
- Retrieval-Augmented Generation (RAG)  
- State-based conversation flows  
- Multi-step lead capture  
- Real LLM integration (Google Gemini)

It is not just a “chatbot” — it is a mini sales system.

---

## 🧠 What This Agent Can Do

The agent can:

- Greet users naturally  
- Answer questions about the product using a knowledge base  
- Detect user intent:  
  - `greeting`  
  - `product_query`  
  - `high_intent`  
- Switch behavior based on intent  
- Guide high-intent users through a funnel:  
  1. Ask for name  
  2. Ask for email  
  3. Ask for platform (YouTube, Instagram, etc.)  
  4. Capture the lead (mocked)  

All of this is controlled using a **LangGraph state machine**, which makes the conversation flow deterministic and production-like.

---

## 🏗 Tech Stack

- Python  
- LangGraph – state-based agent flow  
- FAISS – vector search for RAG  
- HuggingFace Embeddings – document embeddings  
- Google Gemini API – LLM backend  
- RAG (Retrieval-Augmented Generation) – answers come from a knowledge base, not hallucinations  

---

## ⚙️ Setup Instructions

1. Clone the repository:

git clone https://github.com/Khush7349/autostream-lead-agent.git  
cd social-to-lead-agent  

2. Install dependencies:

pip install -r requirements.txt  

3. Create a `.env` file in the root folder:

GEMINI_API_KEY=your_api_key_here  

The `.env` file is ignored by `.gitignore`.  
Never commit your API key.

4. Run the agent:

python main.py  

You should see:

AutoStream Agent is running. Type 'exit' to quit.

---

## 💬 Example Prompts to Try

**Basic**
- Hi  
- What does AutoStream do?  
- What features does AutoStream have?  

**Product-focused**
- Tell me about your pricing  
- What is the difference between Basic and Pro?  
- Does this work for YouTube creators?  

**High-intent**
- I want to use this for my startup  
- This sounds perfect for my channel  
- I want to try the Pro plan  

High-intent messages will automatically trigger the lead capture flow.

---

## 🎯 What This Project Demonstrates

This project shows:

- How AI agents are structured in real systems  
- How to combine LLMs with deterministic logic  
- How RAG prevents hallucination  
- How a chatbot can act like a sales assistant  
- How multi-step workflows can be built with LangGraph  
  
It mirrors how real SaaS companies build intelligent sales assistants.