"""
    Module: handler_states.py
    Author: Rahul George
    
    Description:
    
    License:
    
    Created on: 12-02-2024
    
"""
from enum import Enum


class State(int, Enum):
    OFFLINE = 1
    IDLE = 2
    TESTING = 3
    PAUSED = 4