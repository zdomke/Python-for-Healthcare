
import openai
from openai import OpenAI
import os
import time
import json

with open("keys.json") as f:
    conf = json.load(f)

openai.api_key = conf['api_key']


if __name__ == '__main__':
    os.system('clear')
    print('Welcome to the Stanford Medical AI Assistant!')
    print('How can I help you today?')
    prompt = input('Enter your question here. When you are done, simply enter \'done\' to exit: ')
    while True:
        if prompt == 'done':
            os.system('clear')
            print('Thank you for visiting us. Have a Nice day! Goodbye.')
            break
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=conf['client_key'],
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        os.system('clear')
        print('Working on your request...')
        time.sleep(5)
        os.system('clear')
        print(chat_completion.choices[0].message.content)
        print('\n')
        prompt = input('Do you have any additional questions?\nWhen you are done, simply enter \'done\' to exit: ')

