import random
import string


def generate_referrer_code(length):
    symbols = string.ascii_lowercase + string.digits
    return ''.join(random.sample(symbols, length))