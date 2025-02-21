import openai
import streamlit as st


OPENAI_API_KEY = "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"

st.title("Chatbot")

def chatbot_response(user_text):
    try:
        openai.api_key = OPENAI_API_KEY


        prompt = f"You: {user_text}\nBot:"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,  
            n=1,
            stop=None,
            temperature=0.7,
        )

        bot_reply = response["choices"][0]["text"].strip()

        return bot_reply

    except Exception as e:
        return f"An error occurred: {str(e)}"

def user_input():
    input_text = st.text_input("You: ")
    return input_text

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_text = user_input()

if user_text:
    bot_reply = chatbot_response(user_text)
    st.session_state['chat_history'].append({"user": user_text, "bot": bot_reply})


for entry in st.session_state['chat_history']:
    st.text(f"You: {entry['user']}")
    st.text(f"Bot: {entry['bot']}")