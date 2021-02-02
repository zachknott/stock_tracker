from main import main
import os
import time as t

def run_main():
    try:
        main()
    except:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("Main crashed, restarting")
        t.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear') 

while(True):
    try:
        run_main()
    except:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("Run Main Crashed, restarting")
        t.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    
