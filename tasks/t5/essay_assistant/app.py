import uvicorn
from aidial_client import AsyncDial

from aidial_sdk import DIALApp
from aidial_sdk.chat_completion import ChatCompletion, Request, Response

SYSTEM_PROMPT = """You are an essay-focused assistant. Respond to every request by writing a **short essay** of up to 300 tokens.

**Structure:**
- Clear introduction with thesis
- Body paragraphs with supporting points
- Concise conclusion

**Rules:**
- Always write in essay format regardless of topic
- Keep responses analytical and structured
- Use formal, academic tone
- Include specific examples when relevant
- Maintain logical flow between paragraphs
"""


class EssayAssistantApplication(ChatCompletion):


    async def chat_completion(
            self, request: Request, response: Response
    ) -> None:
        client: AsyncDial = AsyncDial(
            base_url="http://localhost:8080",
            api_key="dial_api_key",
            api_version="2025-01-01-preview"
        )

        with response.create_single_choice() as choice:
            chunks = await client.chat.completions.create(
                deployment_name="claude-3-7-sonnet@20250219",
                stream=True,
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": request.messages[-1].content
                    }
                ],
            )

            async for chunk in chunks:
                if chunk.choices and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if delta and delta.content:
                        choice.append_content(delta.content)


app: DIALApp = DIALApp()
app.add_chat_completion(deployment_name="essay-assistant", impl=EssayAssistantApplication())

if __name__ == "__main__":
    uvicorn.run(app, port=5025, host="0.0.0.0")