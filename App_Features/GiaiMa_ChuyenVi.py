from PY_UI.GiaiMa_ChueynVi import Ui_MainWindow as GMChuyenVi
from PyQt6 import QtWidgets
from ThuatToan.ChuyenViNhieuDong import CChuyenViNhieuDong
import FileHelper as file

class GiaiChuyenVi(GMChuyenVi):
    def __init__(self):
        super(GMChuyenVi,self).__init__()

    def Click_PBRefresh(self):
        self.lE_FileIn.setText('')
        self.tB_Content.setText('')

    def ChooseFileIn(self):
        filePath = file.ChooseFileFromDevice()
        self.lE_FileIn.setText(filePath)
    
    def Click_PBGiaiMa(self):
        fileIn = self.lE_FileIn.text()
        key = [1,5,6,7,2,3,9]
        msg = QtWidgets.QMessageBox()
        try:
            contentFileIn = file.ReadDataInFile(fileIn)
            stringFileIn = ''.join(contentFileIn)
            chuyenvi = CChuyenViNhieuDong('', key, stringFileIn)
            plantText = chuyenvi.GiaiMa()
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
            file.WriteDataInFileOut(listData, 'Text\Decrypt_ChuyenVi')
            msg.setInformativeText('Lưu thành công file: ')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()