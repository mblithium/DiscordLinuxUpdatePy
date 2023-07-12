import requests 
import tarfile
from os import path, makedirs
from shutil import rmtree

NameOfUpdateFile = "discordUpdate.tar.gz"

def downloadUpdateFile():
    DOWNLOADURLDISCORDSTABLE = "https://discord.com/api/download/stable?platform=linux&format=tar.gz"

    try:
        updateFile = requests.get(DOWNLOADURLDISCORDSTABLE, allow_redirects=True)

        open(f'/tmp/{NameOfUpdateFile}', 'wb').write(updateFile.content)
    except:
        print("Error when trying to download update package.")

def applyUpdateToOpt():
    if not path.exists('Discord'): makedirs('Discord')

    try:
        fileUpdate = tarfile.open(f'/tmp/{NameOfUpdateFile}')
        fileUpdate.extractall('/opt')
        fileUpdate.close()
    except:
        print("Error when trying to extract updates for opt/Discord.")

downloadUpdateFile()
applyUpdateToOpt()