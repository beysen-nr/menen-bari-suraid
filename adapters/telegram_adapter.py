from infrastructure.telegram_service import bot
from adapters.openai_adapter import generate_answer

async def message_handler(event):
    print("📩 Incoming:", event.message.text)
    me = await event.client.get_me()

    
    is_bot_reply = event.is_reply
    user_question = event.message.text

    if event.is_group and user_question.startswith(f"@{me.username}"):
        parts = user_question.split()
        if len(parts) > 1:
            command = parts[1].lower()
            remaining_question = " ".join(parts[2:])
        else:
            command = "general"
            remaining_question = ""
        
        original_text = ""
        if is_bot_reply:
            replied = await event.get_reply_message()
            original_text = replied.text
        else:
            original_text = "No specific message, just general question."

        print("🔎 Original:", original_text)
        print("❓ Command:", command)
        print("❓ Question/Arguments:", remaining_question)

        try:
            answer = generate_answer(original_text, command, remaining_question)
            print("✅ Answer:", answer)
        except Exception as e:
            print("❌ GPT Error:", e)
            answer = "⚠️ GPT did not respond."

        await event.reply(answer)