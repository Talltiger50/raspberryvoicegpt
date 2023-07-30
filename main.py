import asyncio
import websockets

async def client():
    # Replace 'PUBLIC_URL' with the actual public URL provided by local tunnel or the server URL
    async with websockets.connect('PUBLIC_URL') as websocket:
        while True:
            message = input("Enter a message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(client())
