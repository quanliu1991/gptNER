import requests
def chatgpt_response(sys_prompt, prompt, model="gpt-3.5-turbo", temperature=0, max_tokens=1024):
    endpoint = "http://36.133.246.107:58080/chatgpt/v1/serving/chatcompletion"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(
            endpoint, json=payload, timeout=5
        )
        response = response.json()
        res = response['choices'][0]['message']['content'].strip()
        if res != "" and res is not None:
            return res
    except Exception as e:
        print(f"{prompt} Error as {e}")
        return ""
    return ""



if __name__ == '__main__':
    a = chatgpt_response(sys_prompt="",prompt="python如何相汉字保存在jsonl文件中")
    print(a)