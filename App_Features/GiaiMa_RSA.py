from PY_UI.GiaiMaRSA import Ui_MainWindow as GMRSA
from PyQt6 import QtWidgets
import FileHelper as file
from ThuatToan.RSA import GiaiMa
listData = []

class GiaiMaRSA(GMRSA):
    def __init__(self):
        super(GiaiMaRSA,self).__init__()

    def Click_PBRefresh(self):
        self.lE_FileIn.setText('')
        self.lE_FileKey.setText('')
        self.tB_Content.setText('')

    def ChooseFileIn(self):
        filePath = file.ChooseFileFromDevice()
        self.lE_FileIn.setText(filePath)

    def ChooseFileKey(self):
        filePath = file.ChooseFileFromDevice()
        self.lE_FileKey.setText(filePath)

    def Click_PBGiaiMa(self):
        fileIn = self.lE_FileIn.text()
        fileKey = self.lE_FileKey.text()
        msg = QtWidgets.QMessageBox()
        try:
            contentFileIn = file.ReadDataInFile(fileIn) 
            contentFileIn = "".join(contentFileIn).split()
            listInt = list(map(int, contentFileIn))
            contentFileKey = file.ReadDataInFile(fileKey)
            privateKey = (int(contentFileKey[0]), int(contentFileKey[1]))
            listNumber = GiaiMa(listInt, privateKey)
            plainText = list(map(str, listNumber))
            global listData
            listData = ''.join(plainText)
            self.tB_Content.setPlainText(listData)
            msg.setInformativeText('Giải mã thành công!')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi: " + str(e))
            msg.setWindowTitle("Error")
            msg.exec()  
            print(e)  

    def Click_PBXuatFile(self):
        fileOut = self.lE_FileOut.text()
        global listData
        msg = QtWidgets.QMessageBox()
        try:
            file.WriteDataInFileOut(listData, fileOut)
            msg.setInformativeText('Lưu thành công file: ' + fileOut)
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()