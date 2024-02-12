"""
    Module: client.py
    Author: Rahul George
    
    Description:
    
    License:
    
    Created on: 12-02-2024
    
"""

from websockets.sync.client import connect

command_map = {
    "1": "place_next_device",
    "2": 'return_device',
    "3": 'press_down',
    "4": 'lift_up',
    '5': 'tcu_set_temperature',
    '6': 'tcu_cancel_temperature',
}


def display_menu():
    print("""1. place_next_device
2. return_device
3. press_down
4. lift_up
5. tcu_set_temperature
6. tcu_cancel_temperature
0. exit""")


i = input("Select \n1. Connect,\n0.Exit\nMake Selection: ")
if i == "1":
    with connect("ws://localhost:8000/ws") as websocket:
        while i != "0":
            print('')
            display_menu()
            i = input("\nMake a selection: ")
            if i != "0" and i in command_map:
                websocket.send(command_map[i])
                msg = websocket.recv()
                print(f">> Received: {msg}")
