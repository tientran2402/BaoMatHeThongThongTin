from PY_UI.GiaiVigenere import Ui_MainWindow as GMVigenre
from PyQt6 import QtWidgets
from ThuatToan.Vigenere import CVigenere
import FileHelper as file

class GiaiVigenere(GMVigenre):
    def __init__(self):
        super(GMVigenre,self).__init__()

    def Click_PBRefresh(self):
        self.lE_FileIn.setText('')
        self.lE_Key.setText('')
        self.tB_Content.setText('')

    def ChooseFileIn(self):
        filePath = file.ChooseFileFromDevice()
        self.lE_FileIn.setText(filePath)
    
    def Click_PBGiaiMa(self):
        fileIn = self.lE_FileIn.text()
        key = self.lE_Key.text()
        msg = QtWidgets.QMessageBox()
        try:
            contentFileIn = file.ReadDataInFile(fileIn)
            stringFileIn = ''.join(contentFileIn)
            vigenre = CVigenere('', key, stringFileIn)
            plantText = vigenre.Decrypt(stringFileIn)
            global listData
            listData = plantText
            self.tB_Content.setPlainText(listData)
            msg.setInformativeText('Giải mã thành công!')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi: " + str(e))
            msg.setWindowTitle("Lỗi")
            msg.exec()  
            print(e)  
    # ==================================================================
    def Click_PBXuatFile(self):
        global listData
        msg = QtWidgets.QMessageBox()
        try:
            file.WriteDataInFileOut(listData, 'Text\Decrypt_Vigenere')
            msg.setInformativeText('Lưu thành công file: ')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()