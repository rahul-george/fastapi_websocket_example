<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">FastAPI Socket Example</h3>

  <p align="center">
    Example project to learn and understand fastapi and socket.
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

I am working on this hardware project where you need to enable socket communication when the hardware is in certain states
The states are defined in this mermaid diagram. 

I created a server which has two endpoints: 
* Post endpoint for changing the states. 
* A web socket endpoint for socket communication. 

Other essential features like workflow dependency and connection manager to restrict the number of connections added. 
Also, developed a client to test it out. 

### Built With

![FastAPI](https://ziadoua.github.io/m3-Markdown-Badges/badges/FastAPI/fastapi1.svg)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Perform the following steps to get started. 
1. Clone the repository
2. Use poetry to install the project dependencies. 
3. Run the server.py 
4. Run the client.py
5. Use the menu in client.py to send appropriate commands. 
6. The server states can be switched via the rest api call /change_state Visit https://localhost/docs to use the swager api to change states. 

