import random
import string


def create_ticket():
    return ''.join(random.choices(string.ascii_letters, k=16))
