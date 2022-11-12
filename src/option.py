from src.util.msg import *

def show_option():
    txt = f"""
    {nomor(1)} Lihat Daftar Karyawan
    {nomor(2)} Tambah Karyawan
    {nomor(3)} Update Karyawan
    {nomor(4)} Hapus Karyawan
    {nomor(5)} Pencatatan Barang
    {nomor(6)} Kasir
    
    {nomor(0)} Exit
    """

    print(txt)