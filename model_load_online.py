import requests
import os

def call_llm(prompt):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    # 从环境变量读取，或在Hugging Face Space设置Secrets
    api_key = os.getenv("SILICON_API_KEY", "sk-ecxatxqjmusubeyvoifnijovrodwkwvcopdkxjtnemrditmh")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "Qwen/Qwen2.5-14B-Instruct",  # 或其他模型
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8,
        "max_tokens": 4096
    }

    res = requests.post(url, headers=headers, json=data)
    return res.json()['choices'][0]['message']['content']

