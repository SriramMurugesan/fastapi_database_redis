import httpx

async def send_to_mcp(text: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:3000/mcp",
            json={"context": {"text": text}}
        )
        return response.json()
