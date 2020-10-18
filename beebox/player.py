import subprocess
import sys
from mpd import MPDClient

def play(file):
    subprocess.run(["aplay", file])

def play_mpd(uri, index=1, isPlaylist=False):
    client = MPDClient()               # create client object
    client.connect("localhost", 6600)  # connect to localhost:66    00
    client.clear()
    
    if (isPlaylist):
        client.load(uri)
    else:
        client.add(uri)
    
    client.play(index)
    client.close()                     # send the close command
    client.disconnect()                # disconnect from the server