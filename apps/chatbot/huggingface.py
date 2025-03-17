import requests
from decouple import config

HUGGINGFACE_API_KEY = config('HUGGINGFACE_API_KEY')


def ask_huggingface(message):
    API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    payload = {
        "inputs": message,
        "parameters": {
            "max_length": 100,
            "temperature": 0.4,
            "top_p": 0.9,
            "do_sample": True
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return f"Error: {response.text}"

        result = response.json()
        generated_text = result[0]['generated_text'].strip()
        print(f"Generated Response: {generated_text}")
        # Detailed logging for debugging
        if isinstance(result, list) and result:
            print(f"Generated Response: {result[0]['generated_text']}")
            return generated_text
        else:
            print("Unexpected response format:", result)
            return "No response from the model."

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "Sorry, I couldn't process that."
