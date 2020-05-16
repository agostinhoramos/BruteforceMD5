from src.lib.algorithm.app import App

app = App()
savepath = "src/data/attack/rainbowtable/Names.txt"
with open("src/data/attack/dictionary/Names.dic", encoding="utf-8", errors="ignore") as fp:
    lines = ""
    line = fp.readline()
    while line :
        word = line.strip()
        lines = lines + app.md5(word)+';'+word+'\n'
        line = fp.readline()
f = open(savepath, "w")
f.write(lines)
f.close()