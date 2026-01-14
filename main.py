import os
from google import genai
from agent.graph import build_graph
from agent.rag import build_vectorstore
class SimpleGemini:
    def __init__(self, model_name: str):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = model_name
    def invoke(self, prompt: str):
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return type("LLMResponse", (), {"content": response.text})
def main():
    llm = SimpleGemini("models/gemini-2.5-flash")
    vectorstore = build_vectorstore()
    app = build_graph(llm, vectorstore)
    print("AutoStream Agent is running. Type 'exit' to quit.\n")
    state = {"messages": []}
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        state["messages"].append({"role": "user", "content": user_input})
        state = app.invoke(state)
        last_item = state["messages"][-1]
        last_msg = last_item["content"] if isinstance(last_item, dict) else last_item
        print(f"Agent: {last_msg}\n")
if __name__ == "__main__":
    main()