from ..algorithm.app import App
import itertools
import threading
import queue
import re

Que = queue.Queue() #FIFO list

class decrypt(App):
    def __init__(self, obj):
        self.OBJ = obj['obj']
        self.SQL = obj['sql']
        self.numThread = 0
        self.numTry = 0
        self.numFound = 0
        hash = self.getJSON(self.OBJ['dir_hostHash'])
        Que.put(hash)

    def getMD5(self):
        arr = []
        count = 0
        group = []
        alist = []
        for _ , values in self.SQL.items():
            for value in values:
                alist.append(value)
                if re.match(r"([a-fA-F\d]{32})", value):
                    group.append(count)
                    arr.append(value)
                count += 1
        if len(arr) > 0:
            self.makeHashFile(alist, group)
        return arr
    
    def makeHashFile(self, alist, group):
        i = j = 0
        if not Que.empty():
            obj = Que.get()
            for h in range(0, len(alist)):
                if h in group:
                    obj.update({alist[h]:{}})
            for attr, values in self.SQL.items():
                for value in values:
                    if i not in group:
                        pos = j%len(group)
                        hash = alist[group[pos]]
                        value = re.sub('[^0-9a-zA-Z]+','', value)
                        if len(value) < 40:
                            obj[hash].update({attr:value})
                        j += 1
                    i += 1
            Que.put(obj)

    def update_data(self, hash, mystr):
        if not Que.empty():
            obj = Que.get()
            try:
                if mystr not in obj[hash]['DecryptedMD5']:
                    obj[hash]['DecryptedMD5'].append(mystr)
            except :
                obj[hash].update({'DecryptedMD5':[mystr]})
                Que.put(obj)
                return 1
            Que.put(obj)

    def MD5byDictionary(self, url, hash):
        # Attempt by dictionary
        self.numThread += 1
        with open(self.OBJ['dir_root']+url, encoding="utf-8", errors="ignore") as fp:
            line = fp.readline()
            while line :
                self.numTry += 1
                word = line.strip()
                
                if self.md5(word) == hash:
                    self.numFound += 1
                    self.update_data(hash, word) #SAVE IT
                    return word
                line = fp.readline()
        return ''
    
    def MD5byWordList(self, url, hash):
        #Attempt by words
        self.numThread += 1
        with open(self.OBJ['dir_root']+url, encoding="utf-8", errors="ignore") as fp:
            line = fp.readline()
            while line :
                self.numTry += 1
                word = line.strip()
                
                if self.md5(word) == hash:
                    self.numFound += 1
                    self.update_data(hash, word) #SAVE IT
                    return word
                line = fp.readline()

        return ''

    def MD5byBruteforce(self, url, hash):
        # Characters attempt
        self.numThread += 1
        groups = self.getJSON(self.OBJ['dir_root']+url)
        for group in groups:
            for i in range(1, len(group)):
                for p in itertools.permutations(group, i):
                    self.numTry += 1
                    newstr = "".join(p)
                    if len(newstr) <= 30: # Password length less than 30
                        newhash = self.md5(newstr)
                        if newhash == hash:
                            self.numFound += 1
                            self.update_data(hash, newstr) #SAVE IT
                            return ''
                    else:
                        return ''

            return ''

    def MD5byRainbowTable(self, url, hash):
        # known hashes attempt
        self.numThread += 1
        with open(self.OBJ['dir_root']+url, encoding="utf-8", errors="ignore") as fp:
            line = fp.readline()
            while line :
                self.numTry += 1
                newline = line.strip() #remove break line
                data = newline.split(';')
                if data[0] == hash:
                    self.numFound += 1
                    self.update_data(hash, data[1]) #SAVE IT
                    return ''
                line = fp.readline()
                
        return ''

class main(App):
    def __init__(self, obj):
        self.OBJ = obj
    
    def exec(self, MD5fn, groups, hashes):
        if not Que.empty():
            threads = []
            for group in groups:
                for hash in hashes:
                    t = threading.Thread(target=MD5fn, args=[group, hash], daemon=True)
                    t.start()
                    threads.append(t)
            for thread in threads:
                thread.join()

            q = Que.get()
            self.setJSON(self.OBJ['dir_hostHash'], q)