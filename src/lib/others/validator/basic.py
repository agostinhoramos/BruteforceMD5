import re
import pathlib

regex = re.compile(
    r"[0-9]\d{,1}$"
)
pattern = re.compile(regex)

def lmt(value, public=False):
    result = pattern.match(value)
    if not public:
        return result

regex = re.compile(
    r"^(?=[a-zA-Z0-9._]{3,20}$)(?!.*[_.]{2})[^_.].*[^_.]$"
)
pattern = re.compile(regex)
def isCredential(val):
    boo = pattern.match(val)
    return bool(boo)


def opc(x):
    if x in ['1','2','3','4']:
        return True
    return False