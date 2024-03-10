from pypresence import Presence
import random
import time

client_id = '1216241049371148369'
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

clip = 0
total_clips = 14

while True:  # The presence will stay on as long as the program is running
    if clip == total_clips+1:
        clip = 0
    print(RPC.update(state="Made by NicePotato",
                     details=f"Clip: {clip+1}/{total_clips}",
                     large_image=f"https://raw.githubusercontent.com/NicePotato-MS/BadAppleRPC/main/clip/c_{clip}.gif"))
    clip=clip+1
    if clip == 14:
        time.sleep(8.28)
    else:
        time.sleep(15)