from src.utils import write_to_file
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
import logging

load_dotenv()
client = OpenAI(
    # this is also the default, it can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)
MAX_LENGTH = 39000


class ChatGPT_2():

    def __init__(self, default_instruction, cache_file_path, default_temp, default_n):
        self.default_instruction = default_instruction
        self.cache_file_path = cache_file_path
        self.cache = self.load_cache()  # Load cache from file
        self.default_temp = default_temp
        self.default_n = default_n
        self.default_instruction = default_instruction

    def load_cache(self):
        if os.path.exists(self.cache_file_path):
            with open(self.cache_file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_cache(self):
        with open(self.cache_file_path, 'w') as f:
            json.dump(self.cache, f)

    def get_response(self, new_question, previous_questions_and_answers=None, author_id=None, problem_id=None, temp=None, n=None, instruction=None):
        messages = [
            {"role": "system",
                "content": instruction if instruction else self.default_instruction},
        ]
        if previous_questions_and_answers:
            for question, answer in previous_questions_and_answers:
                messages.append({"role": "user", "content": question})
                messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": new_question})

        logging.info(f"###CHATGPT_INITIAL_PROMPT###\n\n {messages}")

        prompt = "\n".join([msg['content'] for msg in messages])

        while len(prompt) > MAX_LENGTH:
            # Remove messages from the start until the length is below the threshold
            messages = messages[:3] + messages[5:]
            prompt = "\n".join([msg['content'] for msg in messages])

        if prompt in self.cache:
            return self.cache[prompt]

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
            temperature=temp if temp else self.default_temp,
            n=n if n else self.default_n,
        )
        responses = [choice.message.content for choice in completion.choices]
        self.cache[prompt] = responses
        self.save_cache()  # Save cache to file
        return responses
