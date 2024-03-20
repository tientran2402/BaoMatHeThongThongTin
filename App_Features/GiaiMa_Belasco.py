from PY_UI.GiaiMaBelasco import Ui_MainWindow as GMBelasco
from PyQt6 import QtWidgets
from ThuatToan.Belasco import CBelasco
import FileHelper as file

class GiaiMaBelasco(GMBelasco):
    def __init__(self):
        super(GMBelasco,self).__init__()

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
            belaco = CBelasco(stringFileIn, key)
            plantText = belaco.Decrypt(stringFileIn)
            print(plantText)
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
            file.WriteDataInFileOut(listData, 'Text\Decrypt_Belasco')
            msg.setInformativeText('Lưu thành công file: ')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()