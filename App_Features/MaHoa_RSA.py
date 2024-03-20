from PY_UI.MaHoaRSA import Ui_MainWindow as MHRSA
from PyQt6 import QtWidgets
import FileHelper as file
from ThuatToan.RSA import MaHoa
listData = []
class MaHoaRSA(MHRSA):
    def __init__(self):
        super(MaHoaRSA,self).__init__()

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

    def Click_PBMaHoa(self):
        fileIn = self.lE_FileIn.text()
        fileKey = self.lE_FileKey.text()
        msg = QtWidgets.QMessageBox()
        try:
            contentFileIn = file.ReadDataInFile(fileIn) 
            contentFileIn = "".join(contentFileIn)
            contentFileKey = file.ReadDataInFile(fileKey)
            pulicKey = (int(contentFileKey[0]), int(contentFileKey[1]))
            listInt = MaHoa(contentFileIn, pulicKey)
            listString = list(map(str, listInt)) #Chuyển danh sách số nguyên sang chuỗi
            global listData
            listData = ' '.join(listString)
            self.tB_Content.setPlainText(listData)
            msg.setInformativeText('Mã hóa thành công!')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi: " + str(e))
            msg.setWindowTitle("Lỗi")
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