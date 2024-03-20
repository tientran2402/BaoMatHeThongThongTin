from PY_UI.TaoKhoaRSA import Ui_MainWindow as KeyRSA
from PyQt6 import QtWidgets
import FileHelper as file
from ThuatToan.RSA import TaoKhoa

global_PublicKey = ''
global_PrivateKey = ''
class KeyRSA(KeyRSA):
    def __init__(self):
        super(KeyRSA,self).__init__()

    def click_PBTaoKhoa(self):
        self.tB_PrivateKey.setText('')
        self.tB_PublicKey.setText('')
        public_key, private_key = TaoKhoa()
        e, n = public_key
        d, n = private_key
        
        global global_PrivateKey, global_PublicKey 
        global_PrivateKey = str(d) + '\n' + str(n)
        global_PublicKey = str(e) + '\n' + str(n)
        self.tB_PrivateKey.setText(global_PrivateKey)
        self.tB_PublicKey.setText(global_PublicKey)
    
    # ==================================================================
    def click_PBXuatFile(self):
        msg = QtWidgets.QMessageBox()
        try:
            file.WriteDataInFileOut(global_PublicKey, 'Text\Private_Key.txt')
            file.WriteDataInFileOut(global_PrivateKey, 'Text\Public_Key.txt')
            msg.setInformativeText('Lưu khóa thành công!')
            msg.exec()
        except Exception as e:
            msg.setText("Lỗi: " + str(e))
            msg.setWindowTitle("Error!")
            msg.exec()
