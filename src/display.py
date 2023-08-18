from time import sleep


def char_print(string):
    for character in string[:-1]:
        print(character, end="", flush=True)
        sleep(0.02)
    print(string[-1], flush=True)
    sleep(1)


def char_input(string, title=False, lower=False):
    for character in string:
        print(character, end="", flush=True)
        sleep(0.02)
    sleep(1)

    if title:
        return input().title()
    elif lower:
        return input().lower()
    else:
        return input()
