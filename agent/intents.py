def detect_intent(llm, user_message: str):
    prompt = f"""
You are classifying user intent for a SaaS product called AutoStream.
Classify the user message into exactly one of these categories:
- greeting
- product_query
- high_intent
- chitchat
Rules:
- "hello", "hi", "hey" → greeting
- Asking about pricing, features, plans, support → product_query
- Statements like "I want to sign up", "I want to try Pro", "This sounds good for my startup" → high_intent
- Casual talk like "cool", "nice", "how are you", "okay", "thanks" → chitchat
User message:
"{user_message}"
Respond in this exact format:
intent: <one_of_the_four>
"""
    response = llm.invoke(prompt).content.strip().lower()
    if "greeting" in response:
        return "greeting"
    elif "high_intent" in response:
        return "high_intent"
    elif "chitchat" in response:
        return "chitchat"
    elif "product_query" in response:
        return "product_query"
    else:
        return "product_query"