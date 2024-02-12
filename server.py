"""
    Module: server.py
    Author: Rahul George
    
    Description:
    
    License:
    
    Created on: 12-02-2024
    
"""
import uvicorn
from fastapi import FastAPI

from routes.websocket_routes import router
from utils.handler_states import State
from utils.connection_manager import ConnectionManager

app = FastAPI()

app.handler_state = State.OFFLINE
manager = ConnectionManager()
app.websocket_manager = manager

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app)