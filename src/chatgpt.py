from src.utils import write_to_file
#from openai import OpenAI
import os
import json
#from dotenv import load_dotenv
import logging

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

import gc

# load_dotenv()
# client = OpenAI(
#     # this is also the default, it can be omitted
#     api_key=os.getenv("OPENAI_API_KEY"),
# )
MAX_LENGTH = 10000


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

        print("###Messages###\n\n", messages)
        logging.info(f"###CHATGPT_INITIAL_PROMPT###\n\n {messages}")

        prompt = "\n".join([msg['content'] for msg in messages])

        while len(prompt) > MAX_LENGTH:
            # Remove messages from the start until the length is below the threshold
            messages = messages[:3] + messages[5:]
            prompt = "\n".join([msg['content'] for msg in messages])

        if prompt in self.cache:
            return self.cache[prompt]
        
        print("<#MESSAGES#>", messages)
        print("</#MESSAGES#/>")

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=temp if temp else self.default_temp,
            n=n if n else self.default_n,
        )
        responses = [choice.message.content for choice in completion.choices]
        self.cache[prompt] = responses
        self.save_cache()  # Save cache to file
        return responses


class CodeLlama():

    def __init__(self, default_instruction, cache_file_path, default_temp, default_n, model="codellama/CodeLlama-7b-Instruct-hf"):

        self.default_instruction = default_instruction
        self.cache_file_path = cache_file_path
        self.cache = self.load_cache()  # Load cache from file
        self.default_temp = default_temp
        self.default_n = default_n
        self.default_instruction = default_instruction
        self.inst_sep = '[/INST]'

#         quantization_config = BitsAndBytesConfig(
#             load_in_4bit=True,
#             bnb_4bit_compute_dtype=torch.float16,
#             bnb_4bit_use_double_quant=True,
#         )
        self.model = AutoModelForCausalLM.from_pretrained(
            model,
#             quantization_config=quantization_config,
            device_map="cuda",
            cache_dir="./.models",
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model, use_fast=True, padding_side="left"
        )

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

        print("###Messages###\n\n", messages)
        logging.info(f"###CHATGPT_INITIAL_PROMPT###\n\n {messages}")

        prompt = "\n".join([msg['content'] for msg in messages])

        while len(prompt) > MAX_LENGTH:
            # Remove messages from the start until the length is below the threshold
            messages = messages[:3] + messages[5:]
            prompt = "\n".join([msg['content'] for msg in messages])

        if prompt in self.cache:
            return self.cache[prompt]

        inputs = self.tokenizer.apply_chat_template(messages, tokenize=True, return_tensors="pt").to("cuda")
        # input_ids = inputs.input_ids.to(self.model.device)
        # attention_mask = inputs.attention_mask.to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                # input_ids=input_ids,
                # attention_mask=attention_mask,
                inputs,
                max_length=14000,
                temperature=temp if temp else self.default_temp,
                num_return_sequences=n if n else self.default_n,
                pad_token_id=self.tokenizer.eos_token_id,
                do_sample=True,
            )

        torch.cuda.empty_cache()
        gc.collect()
        responses = [self.tokenizer.decode(
            output, skip_special_tokens=True) for output in outputs]
        
        instruction_responses = [response.split(self.inst_sep, 1)[1] for response in responses]
        self.cache[prompt] = instruction_responses
        self.save_cache()
        return instruction_responses
