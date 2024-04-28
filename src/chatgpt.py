from src.utils import write_to_file
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
import logging

load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),  # this is also the default, it can be omitted
)
MAX_LENGTH = 39000

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
            logging.info(f"###CHATGPT_INITIAL_PROMPT###\n\n {messages}")
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=messages,
                temperature=0
            )
            message = response.choices[0].message.content
            self.cache[prompt] = message
            self.save_cache()  # Save cache to file
            return message
        except Exception as e:
            print("Error:", str(e))
            logging.info(f"###CHATGPT_ERROR###\n\n {str(e)}")

    def get_response(self, new_question, previous_questions_and_answers=None, author_id=None, problem_id=None):
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
        logging.info(f"###CHATGPT_INITIAL_PROMPT###\n\n {messages}")

        write_to_file(f"results_sample/sample_{author_id}_{problem_id}", "prompt.txt", f"\n\n {messages}\n\n")
        
        prompt = "\n".join([msg['content'] for msg in messages])

        while len(prompt) > MAX_LENGTH:
            # Remove messages from the start until the length is below the threshold
            messages = messages[:3] + messages[5:]
            prompt = "\n".join([msg['content'] for msg in messages])
        
        if prompt in self.cache:
            return self.cache[prompt]

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            n=10,
        )
        responses = [choice.message.content for choice in completion.choices]
        self.cache[prompt] = responses
        self.save_cache()  # Save cache to file
        return responses


