"""
    Module: dependencies.py
    Author: Rahul George
    
    Description:
    
    License:
    
    Created on: 12-02-2024
    
"""
from fastapi import Request, HTTPException

from utils.handler_states import State


async def resolve_state(request: Request, state: State):
    current_state = request.app.handler_state
    if current_state == State.OFFLINE and state == State.IDLE:
        print("Ready for use")
        return State.IDLE
    elif current_state == State.IDLE and state == State.OFFLINE:
        print("Ready for shut down")
        return State.OFFLINE
    elif current_state == State.IDLE and state == State.TESTING:
        print("prepare for testing")
        return State.TESTING
    elif current_state == State.TESTING and state == State.PAUSED:
        print("prepare to pause")
        return State.PAUSED
    elif current_state == State.TESTING and state == State.IDLE:
        print("prepare to stop")
        return State.IDLE
    elif current_state == State.PAUSED and state == State.IDLE:
        print("prepare to stop")
        return State.IDLE
    else:
        raise HTTPException(403, "Not an allowed state transition")