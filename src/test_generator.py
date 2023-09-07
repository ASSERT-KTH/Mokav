from chatgpt import ChatGPT_2
import re


class TestGenerator:
    def __init__(self, config):
        self.config = config
        self.chatgpt = ChatGPT_2(
            instruction='Generate Fault-inducing test a test that pass on accepted version and failed on buggy version')
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

    def generate_test3(self, buggy_code, accepted_code, existing_test=None, retry=False):
        responses = []
        if retry:
            prompt = f"both versions give us {retry} as output. The output should be different. Please generate again"
            # chatgpt_resp = self.chatgpt.get_response(new_question=prompt, previous_questions_and_answers=self.prompt_history)
            # print('print chat reps', chatgpt_resp)
            chatgpt_resp = self.chatgpt.get_response(
                new_question=prompt, previous_questions_and_answers=self.prompt_history)
            for i in range(10):
                responses.append(chatgpt_resp[i])
            self.prompt_history.append((prompt, responses[-1]))
        else:
            prompt = f"This is buggy code: ```python {buggy_code}```  This is accepted code: ```python {accepted_code}```   generate a fault inducing testcase in this format: {self.test_format} python dict format between ``` and ``` which accept on accepted version and failed on buggy version without explanation and without '\n' character"

            if self.config == 'BA':
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            elif self.config == 'BAD':
                description = self.code_description(accepted_code)
                prompt += f"  This is description of code: {description}"
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            elif self.config == 'BADT':
                description = self.code_description(accepted_code)
                prompt += f"  This is description: {description}  This is a passing test: ```python {existing_test}```"
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            elif self.config == 'BAT':
                prompt += f"  This is a passing test: {existing_test}"
                chatgpt_resp = self.chatgpt.get_response(new_question=prompt)
                for i in range(10):
                    responses.append(chatgpt_resp[i])
            # for response in responses:
            self.prompt_history.append((prompt, responses[-1]))
        print("###CHATRESP###", responses)
        return [self.extract_regex(str(response)) for response in responses]
