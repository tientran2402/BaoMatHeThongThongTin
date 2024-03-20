
class CVigenere:
    def __init__(self, plainText = '', key = '', cirpherText = ''):
        self.plainText = plainText
        self.key = key
        self.cirpherText = cirpherText
    #========================================================
    def Encrypt(self):
        self.cirpherText = ''
        for i in range(len(self.plainText)):
            c = self.plainText[i]
            vt_key = i % len(self.key)
            if c != ' ':
                so = ord(c)
                so_key = ord(self.key[vt_key]) + 3 #tuyf chinh
                so = (so + so_key) % 65535
                self.cirpherText += chr(so)
            else:
                self.cirpherText += self.key[vt_key]
        return self.cirpherText

    #========================================================
    def Decrypt(self, ci):
        self.plainText = ''
        for i in range(len(ci)):
            c = ci[i]
            vt_key = i % len(self.key)
            if c != self.key[vt_key]:
                so = ord(c)
                so_key = ord(self.key[vt_key]) + 3
                so = (so - so_key + 65535) % 65535
                self.plainText += chr(so)
            else:   
                self.plainText += ' '
        return self.plainText

#========================================================
def Run():
    p =  'Quê hương là chùm khế ngọt \n cho con chèo hái mỗi ngày'
    key = "Phạm Ngọc Mỹ"
    vigenere = CVigenere(p, key)
    c = vigenere.Encrypt()
    print("Sau khi ma hoa: " + c)
    vigenere = CVigenere(p, key, c)
    s = vigenere.Decrypt(c)
    print("Sau khi giai ma: " + s)
#========================================
if __name__=="__main__": #entry point
    Run()
