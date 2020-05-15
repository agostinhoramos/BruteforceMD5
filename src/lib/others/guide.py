import time
import sys

class console:
    def __init__(self, obj):
        self.asw = []
        self.obj = obj

    def progress(self, toolbar_width = 100):
        # setup toolbar
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
        for _ in range(toolbar_width):
            time.sleep(0.1) # do real work here
            # update the bar
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n") # this ends the progress bar
        return False

    def log(self):
        for i in range(0, len(self.obj['ask'][0])):
            while True:
                    inp = input(self.obj['ask'][0][i])
                    try:
                        if bool(self.obj['ask'][1][i][1](inp)):
                            self.asw.append(inp)
                            try:
                                if self.obj['cbk'][i] != None:
                                    self.obj['cbk'][i]()
                                break
                            except:
                                break
                    except:
                        break
                    try:
                        if len(self.obj['ask'][1][i][0]) > 0 :
                            print(self.obj['ask'][1][i][0])
                        continue
                    except:
                        break
        return self.asw