from platform import system
import os

sys = system()

def check():
    if sys == "Windows":
        os.system("cls")
    elif sys == "Darwin":
        os.system("clear")
    elif sys == "Linux":
        os.system("clear")
    else:
        print("Err404-sistem tidak terdeteksi")