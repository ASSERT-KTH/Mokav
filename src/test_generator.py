from src.chatgpt import ChatGPT_2,CodeLlama
import re
import logging


class TestGenerator:
    def __init__(self, config, number_of_samples, temperature):
        self.config = config
        self.chatgpt = CodeLlama(
            default_instruction="You are a software test expert. You are given an original and a patched version of a program. You generate a test input that distinguishes between the two versions. Your generated test input produces different outputs on the original and patched versions.",
            cache_file_path="cache.json",
            default_temp=temperature,
            default_n=number_of_samples
        )
        self.number_of_samples = number_of_samples
        self.temperature = temperature
        self.test_format = "{'inputdata': <inputdata>}"
        self.prompt_history = []

    def extract_code_blocks(self, text):
        code_blocks = re.findall(r"```(.*?)```", text, re.DOTALL)
        return [block.strip() for block in code_blocks]

    def extract_regex(self, string):
        pattern = r"\{'inputdata': '[^']*'\}"
        matches = re.findall(pattern, string)
        return [block.strip() for block in matches]

    def code_description(self, accepted_code):
        description_prompt = f"What is the intention of this code?  {accepted_code}"
        chatgpt_resp = self.chatgpt.get_response(new_question=description_prompt, temp=0, n=1, 
                                         instruction="You are an intelligent software bot that describes python code. You are given a python code snippet.")
        return chatgpt_resp

    def extract_code(self, text):
        pattern = r"```python(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        return "".join([match.strip() for match in matches])

    def generate_test(self, buggy_code, accepted_code, existing_test=None, existing_test_accepted_output=None, 
                      retry_ouput=False, author_id=None, problem_id=None, acc_unique_var_state=None, bug_unique_var_state=None):
        responses = []
        if retry_ouput:
            prompt = f"Both versions give us {retry_ouput} as output. The output should be different."
            if "E" in self.config:
                if acc_unique_var_state is not None:
                    prompt += f""" During the execution of the sample test input on the patched version, variable '{acc_unique_var_state[0]}' gets the value '{acc_unique_var_state[1]}'. This variable never gets this value in the original version.."""
                if bug_unique_var_state is not None:
                    prompt += f""" During the execution of the sample test input on the original version, variable '{bug_unique_var_state[0]}' gets the value '{bug_unique_var_state[1]}'. This variable never gets this value in the patched version.."""
            prompt += " Please generate again"
            chatgpt_resp = self.chatgpt.get_response(
                new_question=prompt, previous_questions_and_answers=self.prompt_history, author_id=author_id, problem_id=problem_id
            )
            
            for i in range(len(chatgpt_resp)):
                responses.append(chatgpt_resp[i])
            self.prompt_history.append((prompt, responses[0]))
        else:
            self.prompt_history = [] # it's an initial prompt

            if "AA" in self.config:
                prompt = f"""
The following is the patched version of a program: 
```python
{accepted_code}```"""

                if 'D' in self.config:
                    acc_description = self.code_description(accepted_code)

                    prompt += f"""
This is a description of the patched program: {acc_description}"""

                prompt += f"""
We also have an original version of this program, which is slightly different from the patched version."""
                
                if "I" in self.config:
                    prompt += f"""
This is a sample test input for which both versions produce the same output: ```python {existing_test}```. The generated output for this sample test input is {existing_test_accepted_output}."""
                    if "E" in self.config:
                        if acc_unique_var_state is not None:
                            prompt += f""" During the execution of the sample test input on the patched version, variable '{acc_unique_var_state[0]}' gets the value '{acc_unique_var_state[1]}'. This variable never gets this value in the original version.."""
                        if bug_unique_var_state is not None:
                            prompt += f""" During the execution of the sample test input on the original version, variable '{bug_unique_var_state[0]}' gets the value '{bug_unique_var_state[1]}'. This variable never gets this value in the patched version."""

                prompt += f"""
Generate a test input in Python dict format as follows:
```python {self.test_format}```
The generated test input should be difference exposing, which means ```python original_func(inputdata)!= patched_func(inputdata)```. This means when the test input is given to the original and patched versions, they should produce different outputs. Your output should not contain any explanation or '\\n' character.
Generate a difference exposing test input as described above.

"""
            elif "BA" in self.config:

                prompt = f"""
The following is the original version of a program: 
```python
{buggy_code}```"""
                if 'D' in self.config:
                    buggy_description = self.code_description(buggy_code)

                    prompt += f"""
This is a description of the original program: {buggy_description}"""
                
                prompt += f"""
The following is the patched version of the program: 
```python
{accepted_code}```"""
                
                if 'D' in self.config:
                    acc_description = self.code_description(accepted_code)

                    prompt += f"""
This is a description of the patched program: {acc_description}"""
                
                if "I" in self.config:                
                    prompt += f"""
This is a sample test input for which both versions produce the same output: ```python {existing_test}```. The generated output for this sample test input is {existing_test_accepted_output}."""
                    if "E" in self.config:
                        if acc_unique_var_state is not None:
                            prompt += f""" During the execution of the sample test input on the patched version, variable '{acc_unique_var_state[0]}' gets the value '{acc_unique_var_state[1]}'. This variable never gets this value in the original version."""
                        if bug_unique_var_state is not None:
                            prompt += f""" During the execution of the sample test input on the original version, variable '{bug_unique_var_state[0]}' gets the value '{bug_unique_var_state[1]}'. This variable never gets this value in the patched version."""

                prompt += f"""
Generate a test input in Python dict format as follows:
```python {self.test_format}```
The generated test input should be difference exposing, which means ```python original_func(inputdata)!= patched_func(inputdata)```. This means when the test input is given to the original and patched versions, they should produce different outputs. Your output should not contain any explanation or '\\n' character.
Generate a difference exposing test input as described above.

"""

            chatgpt_resp = self.chatgpt.get_response(new_question=prompt, author_id=author_id, problem_id=problem_id)
            for i in range(len(chatgpt_resp)):
                responses.append(chatgpt_resp[i])
            
            self.prompt_history.append((prompt, responses[0]))
        print("###CHATRESP###", responses)
        logging.info(f"###CHATRESP###\n\n {responses}")
        return [self.extract_regex(str(response)) for response in responses]
