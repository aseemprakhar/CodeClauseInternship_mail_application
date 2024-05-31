import asyncio
import websockets

async def handle_message(websocket, path):
    async for message in websocket:
        # Broadcast message to all connected clients
        await asyncio.wait([ws.send(message) for ws in connected])

start_server = websockets.serve(handle_message, "localhost", python server.py
)

connected = set()

async def main():
    async with start_server:
        await start_server.serve_forever()

asyncio.run(main())
