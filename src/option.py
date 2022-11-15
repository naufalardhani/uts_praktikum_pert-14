#https://stackoverflow.com/questions/69381312/in-vs-code-importerror-cannot-import-name-mapping-from-collections

from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def show_option():
    questions = [
        {
            'type': 'list',
            'message': 'Select Menu',
            'name': 'inf-opt',
            'choices': [
                Separator('= Karyawan ='),
                {
                    'name': 'Lihat Daftar Karyawan'
                },
                {
                    'name': 'Tambah Karyawan'
                },
                {
                    'name': 'Update Karyawan'
                },
                {
                    'name': 'Hapus Karyawan'
                },
                Separator('= Barang ='),
                {
                    'name': 'Pencatatan Barang'
                },
                {
                    'name': 'Kasir'
                },
                {
                    'name': 'Exit'
                }
            ],
            'validate': lambda answer: 'You must choose at least one topping.' \
                if len(answer) == 0 else True
        }
    ]

    answers = prompt(questions, style=style)
    return answers