from src.chatgpt import ChatGPT_2
import re
import logging


class TestGenerator:
    def __init__(self, config):
        self.config = config
        self.chatgpt = ChatGPT_2(
            instruction="You are a software test expert. You are given an original and a patched version of a program. You generate a test input that distinguishes between the two versions. Your generated test fails on the original version and passes on the patched version.",
            cache_file_path="cache.json"
        )
        self.test_format = "{'inputdata': <inputdata>}"
        self.prompt_history = []
        self.chat_resp_history = []

    def extract_code_blocks(self, text):
        code_blocks = re.findall(r"```(.*?)```", text, re.DOTALL)
        return [block.strip() for block in code_blocks]

    def extract_regex(self, string):
        pattern = r"\{'inputdata': '[^']*'\}"
        matches = re.findall(pattern, string)
        return [block.strip() for block in matches]

    def code_description(self, buggy_code):
        description_prompt = f"What is the intention of this code?  {buggy_code}"
        chatgpt_resp = self.chatgpt.call(description_prompt)
        return chatgpt_resp

    def extract_code(self, text):
        pattern = r"```python(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        return "".join([match.strip() for match in matches])

    def generate_test(self, buggy_code, accepted_code, existing_test=None, retry_ouput=False, author_id=None, problem_id=None):
        responses = []
        if retry_ouput:
            prompt = f"Both versions give us {retry_ouput} as output. The output should be different. Please generate again"
            chatgpt_resp = self.chatgpt.get_response(
                new_question=prompt, previous_questions_and_answers=self.prompt_history, author_id=author_id, problem_id=problem_id
            )
            
            for i in range(10):
                responses.append(chatgpt_resp[i])
            self.prompt_history.append((prompt, responses[-1]))
        else:
            prompt = f"This is buggy code: ```python {buggy_code}```  This is fixed code: ```python {accepted_code}```   generate a fault inducing test case in this format: {self.test_format} python dict format between ``` and ``` which accept on accepted version and failed on the buggy version without explanation and without '\n' character"

            prompt = f"""


"The following is the original version of a program: 
```python {buggy_code}``` 
The following is the patched version of the program: 
```python {accepted_code}```
Generate a test input in Python dict format as follows:
```python {self.test_format}```. The generated test input should be difference exposing, which means the following: when the test input is given to the original and patched versions, they should produce different outputs. Your output should not contain any explanation or '\n' character. 

"""

            if self.config == "BA":
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt, author_id=author_id, problem_id=problem_id)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            elif self.config == "BAD":
                description = self.code_description(accepted_code)
                prompt += f"  This is description of code: {description}"
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt, author_id=author_id, problem_id=problem_id)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            elif self.config == "BADT":
                description = self.code_description(accepted_code)
                prompt += f"  This is description: {description}  This is a passing test: ```python {existing_test}``` generate a diffret test case"
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt, author_id=author_id, problem_id=problem_id)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            elif self.config == "BAT":
                prompt += f"  This is a passing test: {existing_test}"
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt, author_id=author_id, problem_id=problem_id)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            self.prompt_history.append((prompt, responses[-1]))
        print("###CHATRESP###", responses)
        logging.info(f"###CHATRESP###\n\n {responses}")
        return [self.extract_regex(str(response)) for response in responses]
    
    
