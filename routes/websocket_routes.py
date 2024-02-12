"""
    Module: websocket_routes.py
    Author: Rahul George
    
    Description:
    
    License:
    
    Created on: 12-02-2024
    
"""
from fastapi import Request, Depends, APIRouter, WebSocket, WebSocketDisconnect
from utils.handler_states import State
from utils.dependencies import resolve_state

router = APIRouter()

commands = {'place_next_device', 'return_device', 'press_down', 'lift_up', 'tcu_set_temperature', 'tcu_cancel_temperature'}


@router.post("/change_state")
async def change_state(request: Request, next_state: State = Depends(resolve_state)):
    request.app.handler_state = next_state


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    websoc_manager = websocket.app.websocket_manager
    # handler_state = websocket.app.handler_state
    await websoc_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            handler_state = websocket.app.handler_state

            if handler_state is not State.TESTING:
                print(handler_state)
                await websocket.send_text(f"Handler not in testing mode")
                continue

            datalist = data.split()
            if datalist and datalist[0] in commands:
                if datalist[0] == 'place_next_device':
                    print("Next Device placed ")
                    await websocket.send_text("Next device placed")
                elif datalist[0] == 'return_device':
                    await websocket.send_text("Device returned")
                else:
                    await websocket.send_text("Command not implemented")
            else:
                await websocket.send_text(f"Not a valid command. <command> <comma separated args")
    except WebSocketDisconnect:
        websoc_manager.disconnect(websocket)
