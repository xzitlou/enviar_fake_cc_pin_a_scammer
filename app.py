import random

import requests


def generate_random_card():
    card_prefix = ['45', '44', '42']
    rand_card_sufix = [str(random.randint(0, 9)) for c in range(0, 14)]
    card_number = '%s%s' % (
        random.choice(card_prefix),
        ''.join(rand_card_sufix)
    )

    return card_number


def generate_random_pin():
    return ''.join(str(random.randint(0, 9)) for i in range(0, 6))


def generate_random_dni():
    rand_dni_sufix = [str(random.randint(0, 9)) for c in range(0, 7)]
    card_number = '4%s' % ''.join(rand_dni_sufix)

    return card_number


print('== Sending data to scammer ==')
for i in range(10000):
    scammer_url = 'https://ameriquote.com/bcpzonasegurabetaenlinea.vialbcp.com/iniciar-sesion.php'
    card_data = {
        'cardNumber': generate_random_card(),
        'vecla': generate_random_pin()
    }
    print('# Sending card info:', card_data)
    r1 = requests.post(scammer_url, data=card_data)
    print(r1)

    dni_scammer_url = 'https://ameriquote.com/bcpzonasegurabetaenline.vialbcp/operacionesLinea/ajaxProcesos2.php'
    doc_data = {
        'Dni': generate_random_dni(),
        'token': generate_random_pin(),
        'op': 'DniToken'
    }
    print('# Sending document info:', doc_data)
    r2 = requests.post(dni_scammer_url, data=doc_data)
    print(r2)
