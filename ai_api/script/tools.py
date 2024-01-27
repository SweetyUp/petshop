
import os
from openai import OpenAI
API_KEY="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"





import openai
import time
from cprint import cprint

def get_chatgpt_re(prompt, temperature=1.0,api_key=None):
    cprint.ok('==========prompt===================')
    print(prompt)
    cprint.ok('==========prompt over===================')
    if api_key is None:
        # 请在此处提供你的 OpenAI API 密钥
        api_key = API_KEY

    max_retries = 3
    retries = 0

    while retries < max_retries:
        try:
            client = OpenAI(
                # This is the default and can be omitted
                api_key="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",
            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo",
                temperature=temperature
            )
            
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying in 10 seconds...")
                time.sleep(10)
            else:
                raise Exception("Failed after 3 retries")

# # 使用示例
# user_input = "喵喵喵"
# response = get_chatgpt_re(user_input,temperature=1.0)
# print(response)
