import math
class Wronginp(Exception):
    def __init__(self,value):
        self.value=value
        print("Exception")
        return None

class Transpositioncipher:
    def tranencrypt(self,key,msg):
        try:
            if type(msg)!=str:
                raise(Wronginp("string required"))
            self.key=key
            self.msg=msg
            res = [''] * key
            for col in range(key):
                pos = col
                while pos < len(msg):
                    res[col] += msg[pos]
                    pos += key
            return ''.join(res) #Cipher text

        except Wronginp as ex:
            print("Exception raised",ex.value)



    def trandecrypt(self,key,msg):
        try:
            if type(msg)!=str:
                raise(Wronginp("string required"))
            self.key=key
            self.msg=msg
            cols = int(math.ceil(len(msg) / float(key)))
            rows = key
            no_t_box = (cols * rows) - len(msg)
            res = [''] * cols
            col = 0
            row = 0
            for character in msg:
                res[col] += character
                col += 1
                if (col == cols) or (col == cols - 1 and row >= rows - no_t_box):
                    col = 0
                    row += 1
            return ''.join(res)
        except Wronginp as ex:
            print("Exception raised",ex.value)
