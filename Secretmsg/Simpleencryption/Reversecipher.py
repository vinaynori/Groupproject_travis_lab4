class inpsize(Exception):
    def __init__(self,value):
        self.value=value
        print("Exception")
        return None

class Reversecipher:

    def revencrypt(self,msg):
        try:
            if len(msg)<=1:
                raise(inpsize("string length greter than 1 required"))
            self.msg=msg
            res=self.msg[::-1]
            return res
        except inpsize as ex:
            print("Exception raised",ex.value)

    def revdecrypt(self,msg):
        try:
            if len(msg)<=1:
                raise(inpsize("string length greter than 1 required"))
            self.msg=msg
            res=self.msg[::-1]
            return res
        except inpsize as ex:
            print("Exception raised",ex.value)



##Description:
##Inherits features of both Ceasercipher and Doublecipher .
##Eg:- HELLO -> OLLEH -> PMMFI
