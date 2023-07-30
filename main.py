import asyncio
import websockets

async def client():
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key
    async with websockets.connect('ws://raspberry1648.loca.lt') as websocket:
        while True:
            message = input("Enter a message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(client())
