import requests 
import tarfile
from os import path, makedirs, remove
# from shutil import rmtree

NameOfUpdateFile = "discordUpdate.tar.gz"

DISCORD_DOWNLOAD = {
    "STABLE": "https://discord.com/api/download/stable?platform=linux&format=tar.gz",
    "BETA": "https://discord.com/api/download/ptb?platform=linux&format=tar.gz",
    "CANARY": "https://discord.com/api/download/canary?platform=linux&format=tar.gz"
}

def downloadUpdateFile(version):
    try:
        ver_download = version.upper()

        if (path.isfile(f'/tmp/{NameOfUpdateFile}')):
            remove(f'/tmp/{NameOfUpdateFile}')
            
        updateFile = requests.get(DISCORD_DOWNLOAD[ver_download], allow_redirects=True)
        open(f'/tmp/{NameOfUpdateFile}', 'wb').write(updateFile.content)
    except:
        print("Error when trying to download update package.")
        raise Exception()

def applyUpdateToOpt(version):
    match version:
        case "stable":
            if not path.exists('Discord'): makedirs('Discord')
        case "beta":
            if not path.exists('discord-ptb'): makedirs('discord-ptb')
        case "canary":
            if not path.exists('discord-canary'): makedirs('discord-canary')

    try:
        fileUpdate = tarfile.open(f'/tmp/{NameOfUpdateFile}')
        fileUpdate.extractall('/opt')
        fileUpdate.close()
        print("Update completed.")
    except:
        print("Error when trying to extract updates for opt/Discord.")