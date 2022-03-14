from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator

def opciones_vApuesta(answers):
    options = []
    if answers['tApuesta'] == 'color':
        options = ['Rojo', 'Negro']
    if answers['tApuesta'] == 'columna':
        options = ['1', '2', '3']
    if answers['tApuesta'] == 'docena':
        options = ['1', '2', '3']
    if answers['tApuesta'] == 'paridad':
        options = ['Par', 'Impar']
    if answers['tApuesta'] == 'ubicacion':
        options = ['Menor', 'Mayor']
    return options

def parametrizar(r):
    _t = r['tApuesta']
    if (_t == 'docena' or _t == 'columna'):
        r['valor'] = int(r['valor'])
    if (r['capital'] == 'finito'):
        r['capital'] = 0
    else:
        r['capital'] = 1000
        r['mInicial'] = 0
    return r


def menu():
    questions = [
        {
            'type': 'list',
            'name': 'estrategia',
            'message': 'Seleccione estrategia a utilizar en las apuestas',
            'choices': [
                'Dalembert',
                'Fibonacci',
                'Martingala',
            ],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'tApuesta',
            'message': 'Seleccione el tipo de apuesta a realizar',
            'choices': [
                'Color',
                'Columna',
                'Docena',
                'Paridad',
                'Pleno',
                'Ubicacion'
                ],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'input',
            'name': 'valor',
            'message': 'Ingrese el número al cual desea apostar',
            'when': lambda answers: answers['tApuesta'] == 'pleno',
            'validate': lambda val: int(val) >= 0 and int(val) <= 36,
            'filter' : lambda val: int(val)
        },
        {
            'type': 'list',
            'name': 'valor',
            'when': lambda answers: answers['tApuesta'] != 'pleno',
            'message': 'Seleccione el valor al que desea apostar',
            'choices': opciones_vApuesta,
            'filter': lambda val: val.lower()
        },
        {
            'type': 'input',
            'name': 'apInicial',
            'message': 'Ingrese el monto de la apuesta inicial',
            'validate': lambda val: int(val) > 0,
            'filter' : lambda val: int(val)
        },
        {
            'type': 'list',
            'name': 'capital',
            'message': 'Seleccione el tipo de capital a utilizar',
            'choices': [
                'Infinito',
                'Finito'
            ],
            'filter': lambda val: val.lower(),
        },
        {
            'type': 'input',
            'name': 'mInicial',
            'message': 'Ingrese el monto de la banca inicial',
            'when': lambda answers: answers['capital'] == 'finito',
            'filter' : lambda val: int(val),
            'validate': lambda val: int(val) > 0           
        }
    ]
    answers = prompt(questions)
    return parametrizar(answers)

def continuar():
    questions = [
        {
        'type': 'confirm',
        'message': 'Desea realizar otra ejecución?',
        'name': 'continuar',
        'default': True,
        }
    ]
    answers = prompt(questions)
    return answers