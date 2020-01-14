import random
import string

def saltGenerator(length):
    char_set = string.ascii_uppercase + string.digits
    return ''.join(random.sample(char_set*6, length))
