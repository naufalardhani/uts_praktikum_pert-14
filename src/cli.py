import os
import sys
import json

from src.karyawan import Karyawan
from src.banner import show_banner
from src.option import show_option
from src.util.msg import *

def main():
    os.system("clear")
    show_banner()
    k = Karyawan()
    
    while True:
        opt = show_option()['inf-opt']
        if  opt == str("Lihat Daftar Karyawan"):
            k.check_karyawan()
        elif opt == str("Tambah Karyawan"):
            k.add_karyawan()
        elif opt == str("Hapus Karyawan"):
            k.delete_karyawan()
        elif opt == str("Exit"):
            sys.exit()
        else:
            print(f" {failed('Tidak ada')}")
