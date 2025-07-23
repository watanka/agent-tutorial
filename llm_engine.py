from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()


class LLMEngine:
    def __init__(self):
        self.chat_model = OllamaLLM(model="llama3.1")

        # TODO: Tool 사용하도록 수정
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a linux master. You can only answer in linux commands. based on user_input, answer in linux commands.\n\nuser_input: {user_input}",
                )
            ]
        )

    def generate_response(self, user_input):
        if user_input == "exit":
            return "exit"
        prompt = self.prompt_template.invoke({"user_input": user_input})
        response = self.chat_model.invoke(prompt)
        return response
