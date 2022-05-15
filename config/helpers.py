import re
# regex for email
regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check_email(email):
    if re.search(regex, email):
        return True
    else:
        return False