# https://www.freecodecamp.org/news/use-the-rich-library-in-python/
# import main 
from src.config import *
from src.util.msg import *
from src.util.get_json import *
# from src.cli import *

from rich.console import Console
from rich.table import Table
from sys import *
from time import sleep

class Karyawan:
    def __init__(self):
        self.data = {}
        self.umur = []
        self.role = []
        self.database_name = database_name
        self.getDataFromJsonFile = getDataFromJsonFile(self.database_name)

        self.console = Console()

    # def add(self):
    #     self.nama

    def check_karyawan(self):
        data = self.getDataFromJsonFile
        # print(title("Data Karyawan"))
        print()
        if len(data['karyawan']) == 0:
            print(f"    {failed('Data Karyawan Tidak Ditemukan')}")
        elif len(data['karyawan']) >= 0:
            table = Table(title="Data Karyawan")

            table.add_column("ID", justify="center", style="cyan", no_wrap=True)
            table.add_column("Nama", style="magenta")
            table.add_column("Umur", justify="center", style="green")
            table.add_column("Role", justify="left", style="green")

            for i in range(len(data['karyawan'])):
                _id = data['karyawan'][i]['id']
                nama = data['karyawan'][i]['nama']
                umur = data['karyawan'][i]['umur']
                role = data['karyawan'][i]['role']

                table.add_row(str(_id), nama, str(umur), role)

            
            self.console.print(table)

    def add_karyawan(self):
        data = self.getDataFromJsonFile
        _id = 0

        #auto generate id by cek for loop
        for x in range(len(data['karyawan'])):
            _id = x # + 2 


        print()
        # print("\n    [ INPUT KARYAWAN ] \n")
        nama = input(f"    {input_string('Nama > ')}")
        umur = int(input(f"    {input_string('Umur > ')}"))
        role = input(f"    {input_string('Role > ')}")

        karyawan = {
            "id" : str(_id + 2), #auto generate id by + 2
            "nama": nama,
            "umur": umur,
            "role": role
        }
        data['karyawan'].append(karyawan)
        with open("db.json", "w") as connect:
            json.dump(data, connect)
            # print("    Data telah berhasil ditambahkan")
            print(f"\n    {success('Data sukses ditambahkan!')}")

    def delete_karyawan(self):
        data = self.getDataFromJsonFile

        _id = input(f"\n    {input_string('ID Karyawan > ')} ")

        # if data['karyawan'][_id - 1] == None:
        #     print("Tidak ada")

        # for karyawan in data['karyawan']:
        #     if karyawan['id'] == _id:
        #         print(karyawan['nama'])

        # verif = input("Hapus? (y/n) ")
        # if verif == "n":
            # main.main()
            # main()

        finder = False
        for karyawan in data['karyawan']:
            if karyawan['id'] == _id:
                print()
                with self.console.status("[bold green]Deleting data...") as status:
                    sleep(1)
                    data['karyawan'].pop(data['karyawan'].index(karyawan))
                    self.console.log(f" Id {_id} deleted!")
                finder = True
                # print(f"Berhasil menghapus id{_id} dari database!")
                break
        # with open("db.json", "w") as connect:
        #     json.dump(data, connect)
        if finder == False:
            print(f"\n    {failed('ID tidak ditemukan!')}  ")


        # print("\n   [ DELETE KARYAWAN ] \n")


        
        
        # return j['karyawan'][1]['nama']