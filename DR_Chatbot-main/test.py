import requests
import time

# Your OpenAI API key
OPENAI_API_KEY = "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"

# Endpoint for GPT-3.5-turbo
url = "https://api.openai.com/v1/engines/gpt-3.5-turbo/completions"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "OpenAI-Organization": "org-WB8yhTiAbOmZhoaEeXdMhG84",
    "Content-Type": "application/json"
}

# Function to make an API call
def call_gpt3(prompt):
    data = {
        "model": "gpt-gpt-3.5-turbo-1106",
        "prompt": prompt,
        "max_tokens": 500  # Adjust as needed
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to track spending
def track_spending():
    total_spent = 0.0
    cost_per_call = 0.02  # Adjust based on your pricing

    while total_spent < 1.00:
        response = call_gpt3("Translate the following English text to French: 'Hello, world!'")
        total_spent += cost_per_call
        print("Spent so far:", total_spent)
        time.sleep(1)  # To avoid hitting rate limits

    print("Target spending reached!")

# Run the tracking function
track_spending()
