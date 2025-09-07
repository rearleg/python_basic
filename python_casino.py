import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


colors = [
    "\033[31m",
    "\033[33m",
    "\033[32m",
    "\033[36m",
    "\033[34m",
    "\033[35m",
]
reset = "\033[0m"

def rainbow_print(text):
    result = ""
    i = 0
    for ch in text:
        if ch == " " or ch == "\n":
            result += ch
        else:
            result += colors[i % len(colors)] + ch + reset
            i += 1
    print(result)

welcome = """
              _                            _        
             | |                          | |       
__      _____| | ___ ___  _ __ ___   ___  | |_ ___  
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
 \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
                                                    
                                                    
             _   _                                  
            | | | |                                 
 _ __  _   _| |_| |__   ___  _ __                   
| '_ \| | | | __| '_ \ / _ \| '_ \                  
| |_) | |_| | |_| | | | (_) | | | |                 
| .__/ \__, |\__|_| |_|\___/|_| |_|                 
| |     __/ |                                       
|_|    |___/                                        
               _                                    
              (_)                                   
  ___ __ _ ___ _ _ __   ___                         
 / __/ _` / __| | '_ \ / _ \                        
| (_| (_| \__ \ | | | | (_) |                       
 \___\__,_|___/_|_| |_|\___/                        
"""

win = """
                  ___           ___                    ___           ___           ___     
                 /\  \         /\  \                  /\  \         /\  \         /\  \    
      ___       /::\  \        \:\  \                _\:\  \       /::\  \        \:\  \   
     /|  |     /:/\:\  \        \:\  \              /\ \:\  \     /:/\:\  \        \:\  \  
    |:|  |    /:/  \:\  \   ___  \:\  \            _\:\ \:\  \   /:/  \:\  \   _____\:\  \ 
    |:|  |   /:/__/ \:\__\ /\  \  \:\__\          /\ \:\ \:\__\ /:/__/ \:\__\ /::::::::\__\
  __|:|__|   \:\  \ /:/  / \:\  \ /:/  /          \:\ \:\/:/  / \:\  \ /:/  / \:\~~\~~\/__/
 /::::\  \    \:\  /:/  /   \:\  /:/  /            \:\ \::/  /   \:\  /:/  /   \:\  \      
 ~~~~\:\  \    \:\/:/  /     \:\/:/  /              \:\/:/  /     \:\/:/  /     \:\  \     
      \:\__\    \::/  /       \::/  /                \::/  /       \::/  /       \:\__\    
       \/__/     \/__/         \/__/                  \/__/         \/__/         \/__/    

Game End
"""

clear()
rainbow_print(welcome)

pc_choice = random.randint(1, 100)
playing = True

while playing:
    user_choice = int(input("@@@ Choose number @@@ \nYour Answer(1-100): "))
    if user_choice == pc_choice:
        clear()
        rainbow_print(win)
        playing = False
    elif user_choice > pc_choice:
        clear()
        print("Lower!")
    else:
        clear()
        print("Higher!")