import os
import openai


API_KEY = os.getenv('OPENAI_API_KEY')

# Make sure to initialize the OpenAI key


def compose_conversation(history, new_message, system_message=None):
    # Prepend system message to history if provided
    if system_message:
        history.insert(0, {"role": "system", "content": system_message})
    # Append user's message to history
    if new_message:
        history.append({"role": "user", "content": new_message})
    return history

def generate_chat_response(conversation, chatbot):
    # Read the system message from prompt.txt
    with open(f'prompt{chatbot}.txt', 'r') as file:
        system_message = file.read().strip()  # Read and strip any excess whitespace

    updated_conversation = compose_conversation(conversation, '', system_message)

    #print(f"Sending conversation to OpenAI: {updated_conversation}")
    response = openai.chat.completions.create(model="gpt-3.5-turbo-1106",
    messages=updated_conversation,
    stream=True)
    try:
        #print("Response from OpenAI: ", response)
        for message in response:
            print("Message: ", message.choices[0].delta.content)
            if message.choices[0].delta.content != None:
                yield message.choices[0].delta.content
                pass

    except:
        print("Error: ", response)
        # yield "Sorry, I'm having trouble understanding you right now. Please try again later."