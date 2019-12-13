class Wronginp(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return (repr(self.value))


class Ceasercipher:
    def __init__(self,key):
        self.key=key

    def ceaserencrypt(self,msg):
        try:
            if type(msg)!= str:
                raise(Wronginp("string required"))
            self.msg=msg
            alphabet="abcdefghijklmnopqrstuvwxyz"
            newmsg=""
            flag=0
            for character in self.msg:
                if character >= 'A' and character <= 'Z':
                    flag=1
                elif character >= 'a' and character <='z':
                    flag=0
                else:
                    flag=2
                if flag!=2:
                    character=character.lower()
                    pos=alphabet.find(character)
                    newpos=(pos+self.key)%26
                    newchar=alphabet[newpos]
                    if flag==1:
                        newchar=newchar.upper()
                else:
                    newchar=chr(ord(character)+self.key)
                newmsg+=newchar
            return newmsg
        except Wronginp as ex:
            print("Exception raised",ex.value)

    def ceaserdecrypt(self,msg):
        try:
            self.msg=msg
            if type(self.msg)!= str:
                raise(Wronginp("string required"))
            alphabet="abcdefghijklmnopqrstuvwxyz"
            newmsg=""
            flag=0
            for character in self.msg:
                if character >= 'A' and character <= 'Z':
                    flag=1
                elif character >= 'a' and character <='z':
                    flag=0
                else:
                    flag=2
                if flag!=2:
                    character=character.lower()
                    pos=alphabet.find(character)
                    newpos=(pos-self.key)%26
                    newchar=alphabet[newpos]
                    if flag==1:
                        newchar=newchar.upper()
                else:
                    newchar=chr(ord(character)-self.key)
                newmsg+=newchar
            return newmsg
        except Wronginp as ex:
            print("Exception raised",ex.value)



##Description
##Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.
##Eg: A->D,B->E
