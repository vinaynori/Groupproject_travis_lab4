import math
class InsizeError(Exception):
    def __init __(self, value):
        self.value = value
    def __str __(self):
        return(repr(self.value ))

class KeystrError(Exception):
    def __init __(self, value):
        self.value = value
    def __str __(self):
        return(repr(self.value ))


class Transpositioncipher:
    def tranencrypt(self,key,msg):
        try:
            if type(key) != int:
                raise(KeystrError("Key is not INT"))
            if len(msg) <= 1:
                raise(InsizeError("Size of msg is not enough!!"))

            self.key=key
            self.msg=msg
            res = [''] * key
            for col in range(key):
                pos = col
                while pos < len(msg):
                    res[col] += msg[pos]
                    pos += key
            return ''.join(res) #Cipher text

        except InsizeError as ex:
            print('Exception raised:',ex.value )
        except KeystrError as ex:
            print('Exception raised:',ex.value )



    def trandecrypt(self,key,msg):
        try:
            if type(key) != int:
                raise(KeystrError("Key is not INT"))
            if len(msg) <= 1:
                raise(InsizeError("Size of msg is not enough!!"))
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
        except InsizeError as ex:
            print('Exception raised:',ex.value )
        except KeystrError as ex:
            print('Exception raised:',ex.value )
