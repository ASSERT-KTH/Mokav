import json
import openai
# import hashlib
import re
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")
# print(os.getenv("API_KEY"))


# class ChatGPT(object):
#     def __init__(self, model="gpt-3.5-turbo", api_key=None,
#                  cache_folder=None, load_from_cache=True, save_to_cache=True):
#         self.model = model
#         if api_key is not None:
#             openai.api_key = api_key
#         self.cache_folder = cache_folder
#         self.load_from_cache = load_from_cache
#         self.save_to_cache = save_to_cache

#     def call(self, prompt, num_of_samples=1, prefix=None):

#         response = None
#         call_params = self.get_call_params(prompt, num_of_samples)
#         cache_file_path = self.get_cache_file_path(prompt, num_of_samples, prefix)

#         if self.load_from_cache and self.cache_folder is not None:
#             if Path(cache_file_path).is_file():
#                 with open(cache_file_path, "r") as file:
#                     json_to_load = json.load(file)
#                     response = json_to_load['response']

#         if response is None:
#             try:
#                 response = openai.ChatCompletion.create(**call_params)
#             except openai.error.InvalidRequestError as e:
#                 response = {
#                     'error': "context_length_exceeded",
#                     'error_message': e.error.message,
#                     'choices': [ {'message': {'content': ""}} ],
#                     'usage': {'total_tokens': prog_params.gpt35_model_token_limit}
#                     }

#             if self.save_to_cache and self.cache_folder is not None:
#                 with open(cache_file_path, "w") as file:
#                     json_to_save = self.get_json_to_save(call_params, response)
#                     file.write(json.dumps(json_to_save, indent=4, sort_keys=True))

#         if 'error' in response:
#             if response['error'] == "context_length_exceeded":
#                 raise openai.error.InvalidRequestError(response['error_message'], None)

#         response_message = [choice['message']['content'] for choice in response['choices']]
#         response_token_usage = response['usage']['total_tokens']
#         return response_message

#     def get_call_params(self, prompt, num_of_samples=1):
#         return {
#             "model": self.model,
#             "messages": prompt,
#             "n": num_of_samples,
#             "temperature": 1,
#             "top_p": 1,
#         }

#     def get_call_hash(self, prompt, num_of_samples=1):
#         call_params = self.get_call_params(prompt, num_of_samples=num_of_samples)
#         return hashlib.md5(str(call_params).encode('utf-8')).hexdigest()

#     def get_cache_file_path(self, prompt, num_of_samples=1, prefix=None):
#         call_hash = self.get_call_hash(prompt, num_of_samples)
#         if prefix is not None:
#             return f"{self.cache_folder}/{prefix}_{call_hash}.json"
#         return f"{self.cache_folder}/{call_hash}.json"

#     def get_json_to_save(self, call_params, response):
#         return {
#             "call": call_params,
#             "response": response
#         }

#     def extract_code_blocks(text):
#         code_blocks = []
#         pattern = r"```(.*?)```"
#         matches = re.findall(pattern, text, re.DOTALL)
#         for match in matches:
#             code_blocks.append(match.strip())
#         return code_blocks

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
            print("###Messages###\n\n",messages)
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
        instruction=self.instruction
        # build the messages
        messages = [
            {"role": "system", "content": instruction},
        ]
        # add the previous questions and answers
        if previous_questions_and_answers:
            for question, answer in previous_questions_and_answers:
                messages.append({"role": "user", "content": question})
                messages.append({"role": "assistant", "content": answer})
        # add the new question
        messages.append({"role": "user", "content": new_question})

        print("###Messages###\n\n",messages)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            # max_tokens=MAX_TOKENS,
            # top_p=1,
            # frequency_penalty=FREQUENCY_PENALTY,
            n=10,
            # presence_penalty=0.6,
        )
        return[choice['message']['content'] for choice in completion['choices']]
        # return completion.choices[0].message.content
