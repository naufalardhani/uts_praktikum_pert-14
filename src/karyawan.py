from src.config import *
from src.util.msg import *
from src.util.get_json import *

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
                nama = data['karyawan'][i]['nama']
                umur = data['karyawan'][i]['umur']
                role = data['karyawan'][i]['role']

                print("    " + nomor(i+1) + "- - - - - - -")
                # print(f"    [{title(f'karyawan={i + 1}')}]")
                print("     | Nama : " + nama)
                print("     | Umur : " + str(umur))
                print("     | Role : " + role)
            print("    [+]")

    def add_karyawan(self):
        data = self.getDataFromJsonFile

        print()
        # print("\n    [ INPUT KARYAWAN ] \n")
        nama = input(f"    {input_string('Nama > ')}")
        umur = int(input(f"    {input_string('Umur > ')}"))
        role = input(f"    {input_string('Role > ')}")

        karyawan = {
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
        for idx, dictionary in enumerate(self.getDataFromJsonFile):
                self.getDataFromJsonFile.pop(idx)


        print("\n   [ DELETE KARYAWAN ] \n")


        
        
        # return j['karyawan'][1]['nama']