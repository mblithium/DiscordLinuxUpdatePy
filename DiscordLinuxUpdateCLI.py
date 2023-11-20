import DLU

def main():
    while True:
        print("""Choose a version to update:
        1) Discord Stable
        2) Discord Beta
        3) Discord Canary
        """)
        userInput = input("> ")
        match userInput:
            case "1":
                DISCORD_VERSION = "stable"
                break
            case "2":
                DISCORD_VERSION = "beta"
                break
            case "3":
                DISCORD_VERSION = "canary"
                break

    DLU.downloadUpdateFile(DISCORD_VERSION)
    DLU.applyUpdateToOpt(DISCORD_VERSION)


main()