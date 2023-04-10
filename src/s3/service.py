import re

from pydantic import EmailStr


def convert_email_to_bucket(email: EmailStr):
    match = re.search(r"^(.+?)@", email)
    if match:
        result = match.group(1)
        return result
    else:
        return "error in converting email:{1} to a bucket name".format(email)
