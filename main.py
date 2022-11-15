import sys

if sys.version[0] == "2":
    exit("\n    INF-EXPRESS is not supported for python 2.x\n")

from src.cli import *

from src.karyawan import Karyawan
from src.banner import show_banner
from src.option import show_option

    

if __name__ == "__main__":
     main()


    # print("hello world!")
    
    # print(x)