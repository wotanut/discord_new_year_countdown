from pypresence import Presence
import time

"""
You need to upload your image(s) here:
https://discordapp.com/developers/applications/<APP ID>/rich-presence/assets
"""

client_id = "926493615084171345"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

# Make sure you are using the same name that you used when uploading the image
RPC.update(details="Time until 2022:",large_image="new_year", large_text="here's to a better 2023",end="1640995200")

while 1:
    time.sleep(15) #Can only update presence every 15 seconds
