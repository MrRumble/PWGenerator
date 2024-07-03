import random

def password_generator():
    ints = '0123456789'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    specials = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    password = []

    password.append(random.choice(ints))
    password.append(random.choice(alphabet))
    password.append(random.choice(alphabet.upper()))
    password.append(random.choice(specials))

    while len(password) < 20:
        password.append(random.choice(ints + alphabet + specials + alphabet.upper()))

    random.shuffle(password)
    return "".join(password)
    

