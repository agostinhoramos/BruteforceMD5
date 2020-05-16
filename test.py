from src.lib.algorithm.app import App

app = App()
savepath = "src/data/attack/rainbowtable/faithwriters.txt"
with open("src/data/attack/wordlist/faithwriters-withcount.txt", encoding="utf-8", errors="ignore") as fp:
    lines = ""
    line = fp.readline()
    while line :
        word = line.strip().split(' ')[-1]
        if len(word)>0:
            lines = lines + app.md5(word)+';'+word+'\n'
        line = fp.readline()
    f = open(savepath, "w")
    f.write(lines)
    f.close()
    print('Done!')