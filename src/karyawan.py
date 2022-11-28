# https://www.freecodecamp.org/news/use-the-rich-library-in-python/

from src.config import *
from src.util.msg import *
from src.util.get_json import *

from rich.console import Console
from rich.table import Table
from PyInquirer import style_from_dict, Token, prompt, Separator

from sys import *
from time import sleep
from random import randint


class Karyawan:
    def __init__(self):
        self.data = {}
        self.umur = []
        self.role = []
        self.database_name = database_name
        self.getDataFromJsonFile = getDataFromJsonFile(self.database_name)

        self.console = Console()

    def check_karyawan(self):
        data = self.getDataFromJsonFile
        if len(data['kiriman']) == 0:
            print(f"{failed('Data pengiriman tidak ditemukan.')}")
        elif len(data['kiriman']) >= 0:
            table = Table(title="INF-Express | List Kiriman")

            table.add_column("No Resi", justify="center", style="cyan", no_wrap=True)
            table.add_column("Nama Pengirim", style="magenta")
            table.add_column("Nama Penerima", style="magenta")
            table.add_column("Kota Asal", justify="left", style="green")
            table.add_column("Kota Tujuan", justify="left", style="green")
            table.add_column("Status", justify="left", style="green")

            for i in range(len(data['kiriman'])):
                resi = data['kiriman'][i]['resi']
                pengirim = data['kiriman'][i]['pengirim']
                penerima = data['kiriman'][i]['penerima']
                asal = data['kiriman'][i]['asal']
                tujuan = data['kiriman'][i]['tujuan']
                status = data['kiriman'][i]['status']

                table.add_row(str(resi), pengirim, penerima, asal, tujuan, status)
            
            self.console.print(table)

    def add_karyawan(self):
        data = self.getDataFromJsonFile
        _id = 0

        def generate_noresi(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)


        # print()
        # print("\n    [ INPUT KARYAWAN ] \n")
        pengirim = input(f"{input_string('Pengirim')}")
        penerima = input(f"{input_string('Penerima')}")
        asal = input(f"{input_string('Asal Kota')}")
        tujuan = input(f"{input_string('Kota Tujuan')}")
        # role = input(f"    {input_string('Role > ')}")

        karyawan = {
            "resi": "INF-" + str(generate_noresi(9)),
            "pengirim": pengirim.title(),
            "penerima": penerima.title(),
            "asal": asal.title(),
            "tujuan": tujuan.title(),
            "status": "Pending"
        }
        data['kiriman'].append(karyawan)
        with open("db.json", "w") as connect:
            json.dump(data, connect)
            print(f"{success('Kiriman baru berhasil ditambahkan!')}\n")

    def delete_karyawan(self):
        data = self.getDataFromJsonFile

        resi = input(f"{input_string('No Resi')}")

        finder = False
        for kiriman in data['kiriman']:
            if kiriman['resi'] == resi:
                print()
                with self.console.status("[bold green]Deleting data...") as status:
                    sleep(1)
                    data['kiriman'].pop(data['kiriman'].index(kiriman))
                    self.console.log(f"Resi {resi} deleted!")
                finder = True
                # print(f"Berhasil menghapus id{_id} dari database!")
                break
        with open("db.json", "w") as connect:
            json.dump(data, connect)
        if finder == False:
            print(f"{failed('No Resi tidak ditemukan!')}  ")

    def update_karyawan(self):
        data = self.getDataFromJsonFile

        # print(data['kiriman']) 

        style = style_from_dict({
            Token.Separator: '#cc5454',
            Token.QuestionMark: '#673ab7 bold',
            Token.Selected: '#cc5454',  # default
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#f44336 bold',
            Token.Question: '',
        })

        jumlah_kiriman = len(data['kiriman'])
        questions = [
            {
                'type': 'list',
                'message': 'Select Menu',
                'name': 'kiriman-opt',
                'choices': [
                    Separator('= Update Kiriman ='),
                    {
                        'name': "By Resi"
                    }
                ],
                'validate': lambda answer: 'You must choose at least one topping.' \
                    if len(answer) == 0 else True
            }
        ]
        answers = prompt(questions, style=style)

        if answers['kiriman-opt'] == "By Resi":
            resi = input(f"{input_string('Masukan No Resi')}")
            for kiriman in data['kiriman']:
                if kiriman['resi'] == resi:
                    print(info("Status > " + kiriman['status']))
                    questions = [
                        {
                            'type': 'list',
                            'message': 'Select New Status',
                            'name': 'status-opt',
                            'choices': [
                                {
                                    'name': "Pending"
                                },
                                {
                                    'name': "On The Way"
                                },
                                {
                                    'name': "Shipped"
                                }
                            ],
                            'validate': lambda answer: 'You must choose at least one topping.' \
                                if len(answer) == 0 else True
                        }
                    ]
                    answers = prompt(questions, style=style)
                    # new_status = input(f"{input_string('Status Baru')}")
                    kiriman['status'] = answers['status-opt']

        with open("db.json", "w") as connect:
            json.dump(data, connect)
            print(f"\n{info('Kiriman baru berhasil ditambahkan!')}\n")
                    
            
        
        # return answerxs


        # print("\n   [ DELETE KARYAWAN ] \n")


        
        
        # return j['kiriman'][1]['nama']