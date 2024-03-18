import random
import string


def random_string(length):
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])


def random_phone():
    return "".join([random.choice(string.digits) for _ in range(10)])


def random_email():
    return random_string(5) + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])