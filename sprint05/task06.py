import re

def valid_email(email):
    try:
        result = re.fullmatch(r"([a-z]+@[a-z.]+)", email)
        result.group()
        return 'Email is valid'
    except:
        return 'Email is not valid'
