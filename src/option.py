#https://stackoverflow.com/questions/69381312/in-vs-code-importerror-cannot-import-name-mapping-from-collections

from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

from src.config import Option

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
            'message': 'Admin Dashboard | Kiriman Page',
            'name': 'inf-opt',
            'choices': [
                {
                    'name': Option.opt1
                },
                {
                    'name': Option.opt5
                },
                {
                    'name': Option.opt2
                },
                {
                    'name': Option.opt3
                },
                {
                    'name': Option.opt4
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