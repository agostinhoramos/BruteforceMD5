from src.lib.algorithm.hack_SQL import hack_SQL
from src.lib.algorithm.app import App

app = App()

hc = hack_SQL({'sql': {'sidecolumn': ', 1, 1, 1, 1, 1', 'serverurl': 'http://localhost/login.php', 'limit': 'LIMIT <%X%>, <%Y%>', 'sep': ', ', 'comment': '#', 'sqlinjectpos': 1, 'field': ['mail', 'pass', 'remember-me'], 'method': 'POST'}, 'obj': {'app_token': '<hack-info>', 'url_website': 'http://localhost/login.php', 'dir_root': '', 'dir_hostHash': 'src/data/hashes/localhost.json', 'dir_bruteforce': 'src/data/bruteforce.json', 'dir_wordlist': 'src/data/wordlist.json', 'dir_rainbowtable': 'src/data/rainbowtable.json', 'dir_dictionary': 'src/data/dictionary.json', 'dir_knownquery': 'src/data/sqlBlind/KnownQueries.json', 'dir_excludeddatabase': 'src/data/sqlBlind/ExcludedDB.json', 'dir_queryinject': 'src/data/sqlBlind/sqlqueries.json', 'dir_querypiece': 'src/data/sqlBlind/sqlslicequery.json'}})

print( app.parseCHAR(['{','-','}'], ', ') )

# rows = hc.SQLfindAll(app.unifyColumn(['id','firstname','email','safeway']), 'tb_student')
# print(rows)

# from src.lib.algorithm.app import App

# app = App()
# savepath = "src/data/attack/rainbowtable/faithwriters.txt"
# with open("src/data/attack/wordlist/faithwriters-withcount.txt", encoding="utf-8", errors="ignore") as fp:
#     lines = ""
#     line = fp.readline()
#     while line :
#         word = line.strip().split(' ')[-1]
#         if len(word)>0:
#             lines = lines + app.md5(word)+';'+word+'\n'
#         line = fp.readline()
#     f = open(savepath, "w")
#     f.write(lines)
#     f.close()
#     print('Done!')