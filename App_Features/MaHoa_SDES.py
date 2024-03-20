from PY_UI.MaHoaSDES import Ui_MainWindow as MHSDES
from PyQt6 import QtWidgets
from ThuatToan.S_DES import MaHoa
import FileHelper as file

class MaHoaSDES(MHSDES):
    def __init__(self):
        super(MHSDES,self).__init__()

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
            cipherText = []
            for data in contentFileIn:
                cipherText.append(MaHoa(data, key))
            global listData
            listData = ''.join(cipherText)
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
            file.WriteDataInFileOut(listData, 'Text\Encrypt_SDES')
            msg.setInformativeText('Lưu thành công file: ')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()