import uvicorn

from aidial_sdk import DIALApp
from aidial_sdk.chat_completion import ChatCompletion, Request, Response


class EchoApplication(ChatCompletion):
    async def chat_completion(
        self, request: Request, response: Response
    ) -> None:
        last_user_message = request.messages[-1]

        with response.create_single_choice() as choice:
            choice.append_content(last_user_message.content or "")


app = DIALApp()
app.add_chat_completion("echo", EchoApplication())

if __name__ == "__main__":
    uvicorn.run(app, port=5022, host="0.0.0.0")