import openai


class ChatBot():
    def __init__(self) -> None:
        openai.api_key = "*sk*-jocTOJLcDM8nA0PXmJ*45T3Blb*kFJdg5ONU2*q1LK6Q4dfLZDE"

    def get_response(self,user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens = 4000,
            temperature = 0.5
        ).choices[0].text
        return response
    


if __name__=="__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("a joke about dogs")
    print(response)

