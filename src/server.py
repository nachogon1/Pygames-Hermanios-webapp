#!/usr/bin/env python

import asyncio
import threading
from _thread import start_new_thread

import websockets

# import socket
# from .constants import SERVER_IP, PORT

# server_ip = SERVER_IP

# server = server_ip
# port = PORT

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.bind((server, port))
# except socket.error as e:
#     str(e)
#
# s.listen(2)
# print("Waiting for a connection, Server Started")
players_list = [1,2,3,4,5,6]
players = {}
player_number = iter(players_list)
async def handler(websocket):
    player2 = next(player_number)
    # player2 = 1
    print("Connected player:", player2)
    while True:
        # try:
        databit = await websocket.recv()
        print("player", player2, "message", databit, "data", type(databit))
        data = eval(databit)
        print(f"data {data}")
        players[player2] = data
        # for p_index in players:
        #     if not players[p_index]:
        #         players.pop(p_index)
        reply = list(players.values())
        print(f"reply {reply}")
        await websocket.send(str(reply))  # str or bytes check faster
            # databit = conn.recv(2048)
            # data = eval(databit.decode("utf-8"))  # TODO change this for json deserializer
            # players[player] = data
            # for p_index in players:
            #     if not players[p_index]:
            #         players.pop(p_index)
            # reply = list(players.values())
            # conn.send(str.encode(str(reply)))
        #
        # except:
        #     break

    # print("Lost connection")
    # conn.close()

async def main():
    async with websockets.serve(handler, "", 8765):
        await asyncio.Future()  # run forever

# def between_callback():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     ws_server = websockets.serve(handler, '', 8765)
#
#     loop.run_until_complete(ws_server)
#     loop.run_forever() # this is missing
#     loop.close()

if __name__ == "__main__":
    # start_new_thread(between_callback, ())
    # daemon server thread:
    # server = threading.Thread(target=between_callback, daemon=True)
    # server.start()
    # client = threading.Thread(target=client)
    # client.start()
    # client.join()

    # ws_server = websockets.serve(handler, "", 8765)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(ws_server)
    # loop.run_forever()
    asyncio.run(main())
    # start_new_thread(threaded_client, (conn, currentPlayer))

