import json
import openai
import re
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")


class ChatGPT_2():

    def __init__(self, instruction):
        self.instruction = instruction

    def call(self, prompt, history=None):
        if history:
            messages = []
            messages.append(
                {"role": "user", "content": f'this is chat history: {history}'})
            messages.append({"role": "user", "content": prompt})
        else:
            messages = [{"role": "user", "content": prompt}]
        try:
            print("###Messages###\n\n", messages)
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages,
                temperature=0.8
            )
            message = response.choices[0].message.content
            return message
        except Exception as e:
            print("Error:", str(e))

    def get_response(self, new_question, previous_questions_and_answers=None):
        instruction = self.instruction
        messages = [
            {"role": "system", "content": instruction},
        ]
        if previous_questions_and_answers:
            for question, answer in previous_questions_and_answers:
                messages.append({"role": "user", "content": question})
                messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": new_question})

        print("###Messages###\n\n", messages)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            n=10,
        )
        return [choice['message']['content'] for choice in completion['choices']]
