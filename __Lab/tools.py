from time import sleep

def typewriter(text, sleep_dur=.05):
    for character in text:
        sleep(sleep_dur)
        print(character, end="", flush=True)
    print("\r")

def intypewriter(text, sleep_dur=.05):
    for character in text:
        sleep(sleep_dur)
        print(character, end="", flush=True)
    output = input()
    print("\r")
    return output
    




if __name__ == '__main__':
    ...