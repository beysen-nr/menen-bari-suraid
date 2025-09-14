from adapters.openai_adapter import generate_answer

def answer_user(original_text: str, user_question: str) -> str:
    return generate_answer(original_text, user_question)
