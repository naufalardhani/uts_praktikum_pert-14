from src.config import *
from src.util.msg import *
from src.util.get_json import *

from sys import *

class Karyawan:
    def __init__(self):
        self.data = {}
        self.umur = []
        self.role = []
        self.database_name = database_name
        self.getDataFromJsonFile = getDataFromJsonFile(self.database_name)

    # def add(self):
    #     self.nama

    def check_karyawan(self):
        data = self.getDataFromJsonFile
        # print(title("Data Karyawan"))
        print()
        if len(data['karyawan']) == 0:
            print(f"    {failed('Data Karyawan Tidak Ditemukan')}")
        elif len(data['karyawan']) >= 0:
            for i in range(len(data['karyawan'])):
                _id = data['karyawan'][i]['id']
                nama = data['karyawan'][i]['nama']
                umur = data['karyawan'][i]['umur']
                role = data['karyawan'][i]['role']

                print("    " + nomor(i+1) + "- - - - - - -")
                print("     | ID   : " + str(_id))
                print("     | Nama : " + nama)
                print("     | Umur : " + str(umur))
                print("     | Role : " + role)
            print("    [+]")

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

        for karyawan in data['karyawan']:
            if karyawan['id'] == _id:
                print(karyawan['nama'])

        verif = input("Hapus? (y/n) ")
        if verif == "n":
            exit()


        finder = False
        for karyawan in data['karyawan']:
            print(karyawan)
            if karyawan['id'] == _id:
                data['karyawan'].pop(data['karyawan'].index(karyawan))
                finder = True
                print(f"Berhasil menghapus id{_id} dari database!")
                break
        with open("db.json", "w") as connect:
            json.dump(data, connect)
        if finder == False:
            print(f"{_id} -Nömrəli ID tapılmadi")


        print("\n   [ DELETE KARYAWAN ] \n")


        
        
        # return j['karyawan'][1]['nama']