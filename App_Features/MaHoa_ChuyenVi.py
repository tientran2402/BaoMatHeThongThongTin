from PY_UI.MaHoa_ChueynVi import Ui_MainWindow as MHChuyenVi
from PyQt6 import QtWidgets
from ThuatToan.ChuyenViNhieuDong import CChuyenViNhieuDong
import FileHelper as file

class MaHoaChuyenVi(MHChuyenVi):
    def __init__(self):
        super(MHChuyenVi,self).__init__()

    def Click_PBRefresh(self):
        self.lE_FileIn.setText('')
        self.tB_Content.setText('')

    def ChooseFileIn(self):
        filePath = file.ChooseFileFromDevice()
        self.lE_FileIn.setText(filePath)
    
    def Click_PBMaHoa(self):
        fileIn = self.lE_FileIn.text()
        key = [1,5,6,7,2,3,9]
        msg = QtWidgets.QMessageBox()
        try:
            contentFileIn = file.ReadDataInFile(fileIn)
            stringFileIn = ''.join(contentFileIn)
            chuyenvi = CChuyenViNhieuDong(stringFileIn, key, '')
            cipherText = chuyenvi.MaHoa()
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
            file.WriteDataInFileOut(listData, 'Text\Encrypt_ChuyenVi')
            msg.setInformativeText('Lưu thành công file: ')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()