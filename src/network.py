# import os
import ast
import asyncio
import platform
# import socket

# from jscode.main import print_js
# from .constants import SERVER_IP, PORT

def print_js(*args, default=True):
    try:
        platform.window.console.log(*args)
        # for i in args:
        #     platform.window.console.log(i)
    except AttributeError:
        pass
    except Exception as e:
        return e
    if default:
        print(*args)

SOCKET_CONNECTION = """
const socket = new WebSocket('ws://3.75.223.152:8765');
window.socket = socket
window.socket.onopen = () => {
  console.log('Socket connected');
  console.log('Hello from network');
};
// Event handler for socket close
window.socket.onclose = () => {
  console.log('Socket connection closed');
};

// Event handler for socket errors
window.socket.onerror = (error) => {
  console.error('Socket error:', error);
};
"""

RECEIVE_DATA = """
// Event handler for receiving messages from the server
window.socket.onmessage = (event) => {
  // console.log('Received message:', event.data);
  // add wait or event listener
  window.message = event.data
};
"""



class Network:
    def __init__(self):
        # self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = SERVER_IP
        # self.port = PORT
        # self.addr = (self.server, self.port)
        # self.p = self.connect()
        # platform.window.eval(SOCKET_CONNECTION)
        pass

    async def connect(self):
        # try:
            # print("socket", socket.gethostname())
            # self.client.connect(self.addr)
        platform.window.eval(SOCKET_CONNECTION)
        await asyncio.sleep(2)
        # except Exception as e:
        #     print_js(e)

    async def send(self, data):
        try:
            SOCKET_SEND = f"""
              // Send data to the server
              // console.log("testito testito")
              // console.log("testito {data}")
              window.socket.send('{data}');
            """
            # self.client.send(str.encode(str(data)))
            platform.window.eval(SOCKET_SEND)
            platform.window.eval(RECEIVE_DATA)
            await asyncio.sleep(0.005)
            content = platform.window.message
            return ast.literal_eval(content)  # TODO fix this
        except Exception as e:
            print_js(e)
