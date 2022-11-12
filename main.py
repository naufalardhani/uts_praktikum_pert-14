import sys
import os

if sys.version[0] == "2":
    exit("\n    INF-EXPRESS is not supported for python 2.x\n")

from src.karyawan import Karyawan

from src.banner import show_banner
from src.option import show_option


if __name__ == "__main__":
    os.system("clear")
    show_banner()
    k = Karyawan()
    
    while True:
        show_option()
        opt = input("    [+] Option > ")
        if opt == str(1):
            k.check_karyawan()
        elif opt == str(2):
            k.add_karyawan()
        elif opt == str(4):
            k.delete_karyawan()
        elif opt == str(0):
            sys.exit()


    # print("hello world!")
    
    # print(x)