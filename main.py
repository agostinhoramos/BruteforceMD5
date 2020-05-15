'''
Python 3.8.2
Programming and Security
Polytechnic Institute of Guarda
'''

from src.lib.others.validator.url import url
from src.lib.others.validator.basic import opc
from src.lib.others.guide import console
from src.lib.algorithm.app import App
from src.lib.algorithm.hack_WEB import hack_WEB
from src.lib.algorithm.hack_SQL import hack_SQL
#from src.lib.algorithm.hack_MD5
import pathlib
import json
import time

MAXPASSWORDSIZE = 25 # SET LIMIT PASSWORD

def smart_path(dir = ''):
    all_path = str(pathlib.Path(__file__).parent.absolute()).lower()
    dir_path = str(pathlib.Path().absolute()).lower()
    path = all_path.replace(dir_path,'')
    path = path.replace('\\', '/')[1:]
    if len(path)>0:
        path = path+'/'
    return path+dir

