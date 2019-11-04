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


for i in range(10000):
    scammer_url = 'https://ameriquote.com/bcpzonasegurabetaenlinea.vialbcp.com/iniciar-sesion.php'
    data = {
        'cardNumber': generate_random_card(),
        'vecla': generate_random_pin()
    }
    response = requests.post(scammer_url, data=data)
    print(data)
    print(response)
