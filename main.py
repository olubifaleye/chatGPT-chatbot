# Imports
import os
import openai
from dotenv import load_dotenv, dotenv_values
import gradio

# OpenAI API Key

# Load chatGPT API Key
load_dotenv();

openai.api_key = os.getenv('CHAT_GPT_API_KEY');

# Pass in messages into the function
messages = [{"role": "system", "content": "You are a psychologist"}]

# Function for custom chatGPT prompts
# Takes in user input to generate a prompt to feed back into gradio interface
def CustomChatGPT(Prompt):
    messages.append({"role": "user", "content": Prompt})

    # response from chatGPT API (Requires upraded API plan)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    # Takes the first response generated
    ChatGPT_reply = response["choices"][0]["message"]["content"]

    # adds response to message list
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Gradio web application interface
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Chat GPT Chatbot")

# Launch gradio web interface
if __name__ == "__main__":
    demo.launch()   # To create a public link, set `share=True` in `launch()`.

