from PY_UI.MaHoaVigenere import Ui_MainWindow as MHVigenere
from PyQt6 import QtWidgets
from ThuatToan.Vigenere import CVigenere
import FileHelper as file

class MaHoaVigenre(MHVigenere):
    def __init__(self):
        super(MHVigenere,self).__init__()

    def Click_PBRefresh(self):
        self.lE_FileIn.setText('')
        self.lE_Key.setText('')
        self.tB_Content.setText('')

    def ChooseFileIn(self):
        filePath = file.ChooseFileFromDevice()
        self.lE_FileIn.setText(filePath)
    
    def Click_PBMaHoa(self):
        fileIn = self.lE_FileIn.text()
        key = self.lE_Key.text()
        msg = QtWidgets.QMessageBox()
        try:
            contentFileIn = file.ReadDataInFile(fileIn)
            stringFileIn = ''.join(contentFileIn)
            vigenere = CVigenere(stringFileIn, key)
            cipherText = vigenere.Encrypt()
            global listData
            listData = cipherText
            self.tB_Content.setPlainText(listData)
            msg.setInformativeText('Mã hóa thành công!')
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
            file.WriteDataInFileOut(listData, 'Text\Encrypt_Vigenere')
            msg.setInformativeText('Lưu thành công file: ')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()