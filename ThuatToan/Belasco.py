#Class Belasco
class CBelasco:
    def __init__(self, plainText, key, cipherText = ''):
        self.plainText = plainText
        self.key = key
        self.cipherText = cipherText
    #================================================
    def Encrypt(self):
        self.cipherText = ''
        for i in range(len(self.plainText)):
            c = self.plainText[i]
            row = (ord(self.key[i % len(self.key)]) +65535) % 65535
            col = (ord(c) + 65535) % 65535
            so = (row + col)
            self.cipherText = self.cipherText + chr(so)
        return self.cipherText
    #=================================================
    def Decrypt(self, ci):
        self.plainText = ''
        for i in range(len(ci)):
            c = ci[i]
            row = (ord(self.key[i % len(self.key)]) + 65535) % 65535
            col = (ord(c) + 65535) % 65535
            so = (col - row)
            self.plainText = self.plainText + chr(so)
        return self.plainText
#========================================
def main():
    # p =  input("Moi nhap chuoi can ma hoa: ")
    p = 'Quê hương là chùm khế ngọt cho con chèo hái mỗi ngày \n Đỗ anh Duy'
    # k =  input("Moi nhap chuoi key: ")
    k = 'Đỗ Anh Duy'
    belaco = CBelasco(p, k)
    ci = belaco.Encrypt()
    print("Sau khi ma hoa= " + ci)
    print("Sau khi giai ma= " + belaco.Decrypt(ci))
#========================================
if __name__=="__main__":
    main() 
