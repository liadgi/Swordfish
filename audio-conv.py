import os
import subprocess

os.remove("eng-test.flac")

command = 'ffmpeg -i eng-test.mp3 -filter:a "atempo=0.8,atempo=0.8" -ab 28000 -ac 1 -ar 16000 -vn eng-test.flac'

subprocess.call(command, shell=True)