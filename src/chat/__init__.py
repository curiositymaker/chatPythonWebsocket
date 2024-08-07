from quart import Quart, render_template, websocket
import random
import string
import uuid

app = Quart(__name__)

@app.route('/')
async def index():
    return await render_template("index.html")

def generate_random_string(length=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@app.websocket('/ws')
async def ws():
    client_id = str(uuid.uuid4())  # Generate a unique client ID
    print(f"New client connected: {client_id}")
    try:
        while True:
            data = await websocket.receive()
            random_string = generate_random_string()
            response = f"Client ID: {client_id}. Server received: {data}. Random string: {random_string}"
            await websocket.send(response)
    finally:
        print(f"Client disconnected: {client_id}")

#simulating dummy response of TTS 
def dummy_speech_generation():
    # Placeholder for TTS functionality
    return "This is a dummy TTS response"

def create_app():
    return app

def run():
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()