import subprocess
import sys
from mpd import MPDClient
import speek

def play(file):
    subprocess.run(["aplay", file])

def play_mpd(uri, index=1, isPlaylist=False):
    client = __get_connected_client()
    client.clear()

    if (isPlaylist):
        client.load(uri)
    else:
        client.add(uri)

    print(uri)
    print(index)

    if (index == 1):
        client.play()
    else:
        client.play(index)

    __disconnect_client(client)

def stop():
    client = __get_connected_client()
    client.stop()
    __disconnect_client(client)

def next():
    client = __get_connected_client()
    status = client.status()
    idx_current_song = int(status["song"])
    playlist_length = int(status["playlistlength"])    
 
    can_play_next = (idx_current_song + 1) < playlist_length
    
    if (can_play_next):
        client.next()

    __disconnect_client(client)

def previous():
    client = __get_connected_client()
    status = client.status()
    idx_current_song = int(status["song"])
 
    can_play_prev = idx_current_song > 0
    
    if (can_play_prev):
        client.previous()

    __disconnect_client(client)

def say(text):
   client = __get_connected_client()
   file = speek.to_file(text, "speech.wav")
   play_mpd(file)
   __disconnect_client(client)

def toggle_pause():
    client = __get_connected_client()
    client.pause()
    __disconnect_client(client)

def __get_connected_client():
    client = MPDClient()               # create client object
    client.connect("localhost", 6600)  # connect to localhost:66    00
    return client

def __disconnect_client(client):
    client.close()                     # send the close command
    client.disconnect()                # disconnect from the server

    
