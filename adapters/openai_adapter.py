from infrastructure.openai_service import ask_gpt

def generate_answer(original_text: str, command: str, user_question: str) -> str:
    """Format prompt for GPT based on the command and get answer."""
    
   
    system_prompt = "You are a helpful assistant. Respond in the same language as the user's request."
    
    
    if command == "summarize":
        user_prompt = f"Please provide a concise summary of the following text:\n\nTEXT: {original_text}"
        max_tokens = 150
    elif command == "translate":
        target_lang = user_question.replace("to", "").strip() or "English"
        user_prompt = f"Translate the following text to {target_lang}:\n\nTEXT: {original_text}"
        max_tokens = 500
    elif command == "fact-check":
        user_prompt = f"Fact-check the following claims and provide sources or context for your findings. If a claim is false, explain why.\n\nCLAIMS: {original_text}"
        max_tokens = 500
    elif command in ["explain", "example", "simplify"]:
        user_prompt = f"I want you to act as a clear, concise expert. Given the following message, can you {command} it for me? Ignore the original message's language and reply in the language of my request.\n\nMessage: {original_text}\n\nMy request: {user_question}"
        max_tokens = 300
    else:
        
        user_prompt = f"Message: {original_text}\n\nQuestion: {user_question}"
        max_tokens = 200

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    return ask_gpt(messages, max_tokens)