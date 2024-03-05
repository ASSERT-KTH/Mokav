import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

class ChatGPT_2():

    def __init__(self, instruction, cache_file_path):
        self.instruction = instruction
        self.cache_file_path = cache_file_path
        self.cache = self.load_cache()  # Load cache from file

    def load_cache(self):
        if os.path.exists(self.cache_file_path):
            with open(self.cache_file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_cache(self):
        with open(self.cache_file_path, 'w') as f:
            json.dump(self.cache, f)

    def call(self, prompt, history=None):
        if prompt in self.cache:
            return self.cache[prompt]

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
            self.cache[prompt] = message
            self.save_cache()  # Save cache to file
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

        prompt = "\n".join([msg['content'] for msg in messages])
        
        if prompt in self.cache:
            return self.cache[prompt]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            n=10,
        )
        responses = [choice['message']['content'] for choice in completion['choices']]
        self.cache[prompt] = responses
        self.save_cache()  # Save cache to file
        return responses
