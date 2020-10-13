import subprocess
import sys

def play(file):
    subprocess.run(["aplay", file])