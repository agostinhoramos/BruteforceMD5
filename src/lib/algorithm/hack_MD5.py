from ..algorithm.app import App
import itertools
import threading
import queue
import hashlib
import re

Que = queue.Queue()

class decrypt(App):
    def __init__(self, obj):
        self.OBJ = obj
        self.passLen = 3 #By default
        self.numThread = 0
        self.numTry = 0
        self.numFound = 0
    
    def setHashPath(self, url):
        Que.put(self.getJSON(url))

    def setPath(self, path):
        self.spath = path

    def MD5HASH(self, my_str):
        m = hashlib.md5()
        m.update(my_str.encode('utf-8')) # Unicode
        return m.hexdigest()
    
    def setPassLen(self, num):
        self.passLen = num

    def getMD5(self):
        arr = []
        count = 0
        group = []
        alist = []
        for _ , values in self.OBJ.items():
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
            for attr, values in self.OBJ.items():
                for value in values:
                    if i not in group:
                        pos = j%len(group)
                        hash = alist[group[pos]]
                        obj[hash].update({attr:value})
                        j += 1
                    i += 1
            Que.put(obj)

    def update_data(self, hash, mystr):
        if not Que.empty():
            obj = Que.get()
            try:
                if mystr not in obj[hash]['MD5Decryption']:
                    obj[hash]['MD5Decryption'].append(mystr)
            except :
                obj[hash].update({'MD5Decryption':[mystr]})
                Que.put(obj)
                return 1
            Que.put(obj)

    def MD5byWord(self, url, hash):
        # Attempt by words
        self.numThread += 1
        with open(self.spath+url, encoding="utf-8", errors="ignore") as fp:
            line = fp.readline()
            while line :
                self.numTry += 1
                line = fp.readline()
                word = line.strip()
                if self.MD5HASH(word) == hash:
                    self.numFound += 1
                    self.update_data(hash, word) #SAVE IT
                    return word
        return ''
    
    def MD5byChar(self, group, hash):
        # Characters attempt
        self.numThread += 1
        for i in range(1, len(group)):
            for p in itertools.permutations(group, i):
                self.numTry += 1
                newstr = "".join(p)
                if len(newstr) <= self.passLen:
                    newhash = self.MD5HASH(newstr)
                    if newhash == hash:
                        self.numFound += 1
                        self.update_data(hash, newstr) #SAVE IT
                        return ''
                else:
                    return ''
        return ''

class main(App):
    def __init__(self):
        pass
    def setHashPath(self, url):
        self.hashFile = url
    
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
        self.setJSON(self.hashFile, Que.get() )