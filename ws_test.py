import asyncio
import websockets

async def test_ws():
    token = "PASTE_YOUR_JWT_TOKEN_HERE"
    uri = f"ws://localhost:8000/ws/testroom?token={token}"
    
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from Python client!")
        response = await websocket.recv()
        print("Server said:", response)

asyncio.run(test_ws())
