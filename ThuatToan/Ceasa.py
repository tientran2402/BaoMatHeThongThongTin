#===========================================
class CCeasar:
    def __init__(self, plainText, key, cipherText = ''):
        self.plainText = plainText
        self.key = key
        self.cipherText = cipherText
   
#     #======================================
#     def GiaiMa(self):
#         self.plainText = ''
#         for c in self.cipherText:
#             so = ord(c)
#             so = (so - self.key)
#             self.plainText = self.plainText + chr(so)
#         return self.plainText
#     #======================================
 #======================================
    def MaHoa(self):
        self.cipherText = ''
        for c in self.plainText:
            so = ord(c)
            so = (so + self.key + 65500) % 65500
            self.cipherText = self.cipherText + chr(so)
        return self.cipherText
# #============================================
def run():
    # p = input('Moi nhap chuoi can ma hoa: ')
    p = "65537"
    key = 1114111000000000
    ceasar = CCeasar(p, key)
    ceasar1 = CCeasar(ceasar.MaHoa(), -key)
    print('Chuoi sau khi ma hoa: '+ ceasar.MaHoa())
    print('Chuoi sau khi ma hoa: '+ ceasar1.MaHoa()) 

if __name__ == '__main__': #entry point
    run()