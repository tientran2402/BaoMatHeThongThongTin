from PyQt6 import QtWidgets
from App_Features.MaHoa_RSA import MaHoaRSA
from App_Features.GiaiMa_RSA import GiaiMaRSA
from App_Features.MaHoa_SDES import MaHoaSDES
from App_Features.GiaiMa_SDES import GiaiMaSDES
from App_Features.TaoKhoa_RSA import KeyRSA
from App_Features.MaHoa_Belasco import MaHoaBelasco
from App_Features.GiaiMa_Belasco import GiaiMaBelasco
from App_Features.MaHoa_Vigenere import MaHoaVigenre
from App_Features.GiaiMa_Vigenere import GiaiVigenere
from App_Features.MaHoa_ChuyenVi import MaHoaChuyenVi
from App_Features.GiaiMa_ChuyenVi import GiaiChuyenVi
import sys
#=====================================================================
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
#=====================================================================
def MH_MaHoaRSA():
    global ui
    ui = MaHoaRSA()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFileIn.clicked.connect(ui.ChooseFileIn)
    ui.pB_ChooseFileKey.clicked.connect(ui.ChooseFileKey)
    ui.pB_Encrypt.clicked.connect(ui.Click_PBMaHoa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_FileOut.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_GM_RSA_2.triggered.connect(MH_GiaiMaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_GM_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#=====================================================================
def MH_GiaiMaRSA():
    global ui
    ui = GiaiMaRSA()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFileIn.clicked.connect(ui.ChooseFileIn)
    ui.pB_ChooseFileKey.clicked.connect(ui.ChooseFileKey)
    ui.pB_Decrypt.clicked.connect(ui.Click_PBGiaiMa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_FileOut.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_GM_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#=====================================================================
def MH_TaoKhoaRSA():
    global ui
    ui = KeyRSA()
    ui.setupUi(MainWindow)
    ui.pB_CreateKey.clicked.connect(ui.click_PBTaoKhoa)
    ui.pB_Decrypt.clicked.connect(MH_GiaiMaRSA)
    ui.pB_Encrypt.clicked.connect(MH_MaHoaRSA)
    ui.pB_LuuFile.clicked.connect(ui.click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_GiaiMaRSA)
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#=====================================================================  
def MH_MaHoaSDES():
    global ui
    ui = MaHoaSDES()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_MaHoa.clicked.connect(ui.Click_PBMaHoa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere) 
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#=====================================================================    
def MH_GiaiMaSDES():
    global ui
    ui = GiaiMaSDES()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_GiaiMa.clicked.connect(ui.Click_PBGiaiMa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#===================================================================== 
def MH_MaHoaBelasco():
    global ui
    ui = MaHoaBelasco()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_MaHoa.clicked.connect(ui.Click_PBMaHoa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES)  
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)  
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#===================================================================== 
def MH_GiaMaBelasco():
    global ui
    ui = GiaiMaBelasco()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_GiaiMa.clicked.connect(ui.Click_PBGiaiMa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES) 
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#=====================================================================  
def MH_MaHoaVigenere():
    global ui
    ui = MaHoaVigenre()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_MaHoa.clicked.connect(ui.Click_PBMaHoa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES) 
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Vigenre.triggered.connect(MH_GiaiMaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#========================================================== 
def MH_GiaiMaVigenere():
    global ui
    ui = GiaiVigenere()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_MaHoa.clicked.connect(ui.Click_PBGiaiMa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES) 
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi) 
#==========================================================
def MH_MaHoaChuyenVi():
    global ui
    ui = MaHoaChuyenVi()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_MaHoa.clicked.connect(ui.Click_PBMaHoa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES) 
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_GM_ChuyenVi.triggered.connect(MH_GiaiMaChuyenVi)
#============================================================= 
def MH_GiaiMaChuyenVi():
    global ui
    ui = GiaiChuyenVi()
    ui.setupUi(MainWindow)
    ui.pB_ChooseFile.clicked.connect(ui.ChooseFileIn)
    ui.pB_GiaiMa.clicked.connect(ui.Click_PBGiaiMa)
    ui.pB_Refresh.clicked.connect(ui.Click_PBRefresh)
    ui.pB_LuuFile.clicked.connect(ui.Click_PBXuatFile)
    ui.ac_MH_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_RSA_2.triggered.connect(MH_MaHoaRSA)
    ui.ac_GM_TaoKhoa.triggered.connect(MH_TaoKhoaRSA)
    ui.ac_MH_TaoKhoa.triggered.connect(MH_TaoKhoaRSA) 
    ui.ac_GM_SDES.triggered.connect(MH_GiaiMaSDES) 
    ui.ac_MH_SDES.triggered.connect(MH_MaHoaSDES)
    ui.ac_MH_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_GM_Belasco.triggered.connect(MH_MaHoaBelasco)
    ui.ac_MH_Vigenere.triggered.connect(MH_MaHoaVigenere)
    ui.ac_MH_ChuyenVi.triggered.connect(MH_MaHoaChuyenVi)
#============================================================       
if __name__ == "__main__":
    MH_MaHoaRSA() 
    MainWindow.show()
    sys.exit(app.exec())