from pypresence import Presence
import random
import time

client_id = '1216241049371148369'
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

clip = 1
total_clips = 218

while True:  # The presence will stay on as long as the program is running
    if clip == total_clips:
        clip = 1
    print(RPC.update(state="Made by NicePotato",
                     details="Clip: "+str(clip)+"/"+str(total_clips),
                     large_image=""))
    clip=clip+1
    time.sleep(1)