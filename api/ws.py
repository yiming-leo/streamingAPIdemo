from fastapi import FastAPI, WebSocket, APIRouter
from starlette.websockets import WebSocketDisconnect

app = FastAPI()
router = APIRouter()

# target url: ws://localhost:8000/ws


# obey the target url
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # protocol http -> ws
    await websocket.accept()
    try:
        # loop listening
        while 1:
            data = await websocket.receive_text()
            await websocket.send_text(f"received: {data}")
    except WebSocketDisconnect:
        print("WS Disconnected")
