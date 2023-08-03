import openai


class ChatBot():
    def __init__(self) -> None:
        openai.api_key = ""

    def get_response(self,user_input):
        response = openai.completion.create(
            engine = "text-davinci-003",
            prompt = user_input
        )
