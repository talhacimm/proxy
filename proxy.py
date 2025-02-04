import os
import time

def colored_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, colors['white'])}{text}{colors['reset']}"

def display_ascii_art():
    art = '''\033[93m
▄▄▄▄·  ▄▄▄· ▄ •▄ ▪  • ▌ ▄ ·. ·▄▄▄▄   ▄▄▄· 
▐█ ▀█▪▐█ ▀█ █▌▄▌▪██ ·██ ▐███▪██▪ ██ ▐█ ▀█ 
▐█▀▀█▄▄█▀▀█ ▐▀▀▄·▐█·▐█ ▌▐▌▐█·▐█· ▐█▌▄█▀▀█ 
██▄▪▐█▐█ ▪▐▌▐█.█▌▐█▌██ ██▌▐█▌██. ██ ▐█ ▪▐▌
·▀▀▀▀  ▀  ▀ ·▀  ▀▀▀▀▀▀  █▪▀▀▀▀▀▀▀▀•  ▀  ▀ 
\033[0m'''
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'] 
    for i in range(10):
        color = colors[i % len(colors)]
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(colored_text(art, color))
        time.sleep(0.5)

def main():
    if os.name == 'nt':
        os.system("title DARK PROXY V1")
    else:
        os.system("echo -e '\033]0;Bakımda.\007'")
    display_ascii_art()

if __name__ == "__main__":
    main()
