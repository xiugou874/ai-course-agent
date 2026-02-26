import requests

def call_llm(prompt):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}

    data = {
        "model": "qwen2.5-14b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8
    }

    res = requests.post(url, headers=headers, json=data)
    return res.json()['choices'][0]['message']['content']


