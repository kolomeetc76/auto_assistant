import glob
import os
import os.path
import shutil
import threading
import urllib.request
from subprocess import call
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel, QMessageBox, QProgressBar
import sys
import time


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setFixedSize(320, 400)
        Dialog.setWindowIcon(QtGui.QIcon('ico.ico'))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 20, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 70, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 120, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 170, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 270, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 320, 131, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 220, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")


        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 210, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labl = QLabel(Dialog)
        self.labl.setGeometry(10, 10, 10, 10)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.download_vpn()
        self.download_rt()
        self.download_des()
        self.download_utm()
        self.move_to_config()
        self.firewall_button()
        self.service_button()
        


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UTM Настройка"))
        self.pushButton.setText(_translate("Dialog", "Скачать Open VPN"))
        self.pushButton_2.setText(_translate("Dialog", "Скачать Рутокен"))
        self.pushButton_3.setText(_translate("Dialog", "Скачать DXBX Desktop"))
        self.pushButton_4.setText(_translate("Dialog", "Скачать UTM"))
        self.pushButton_7.setText(_translate("Dialog", "Config и Transport"))
        self.pushButton_5.setText(_translate("Dialog", "Настроить Брандмауэр"))
        self.pushButton_6.setText(_translate("Dialog", "Перезапустить службы"))
        
# download_vpn
    def download_vpn(self):
        self.pushButton.clicked.connect(self.vpn_download)

    def vpn_download(self):
        link1 = 'https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.9-I601-Win10.exe'
        filename = link1.split('/')[-1]
        print (filename)
        r = requests.get(link1)
        open(filename, 'wb').write(r.content)


# Download rtDriver
    def download_rt(self):
        self.pushButton_2.clicked.connect(self.rutoken_download)

    def rutoken_download(self):
        class GeeksforGeeks(QDialog):
 
            def __init__(self):
                super().__init__()
         
                # calling a defined method to initialize UI
                self.init_UI()
         
            # method for creating UI widgets
            def init_UI(self):
                self.setFixedSize(300, 100)
                self.setWindowIcon(QtGui.QIcon('ico.ico'))
                self.progressBar = QProgressBar(self)
                self.progressBar.setGeometry(25, 45, 210, 30)        
                self.button = QPushButton('Скачать', self)
                self.button.move(220, 45)
                self.button.clicked.connect(self.Download)
                self.setGeometry(310, 310, 280, 170)
                self.setWindowTitle("Download rtDriver")

                self.show()
        #close from xmark
            def closeEvent(self, init_UI):
                GeeksforGeeks.destroy(self)
         
            # when push button is pressed, this method is call
            def Handle_Progress(self, blocknum, blocksize, totalsize):
         
                ## calculate the progress
                readed_data = blocknum * blocksize
         
                if totalsize > 0:
                    download_percentage = readed_data * 100 / totalsize
                    self.progressBar.setValue(download_percentage)
                    QApplication.processEvents()


            # method to download any file using urllib
            def Download(self):
         
                # specify the url of the file which is to be downloaded
                down_url = 'https://download.rutoken.ru/Rutoken/Drivers/Current/rtDrivers.exe' # specify download url here
         
                # specify save location where the file is to be saved
                save_loc = 'rtDrivers.exe'
         
                # Downloading using urllib
                urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)

                GeeksforGeeks.destroy(self)

        if __name__ == '__main__':
            App = QApplication(sys.argv)
            window = GeeksforGeeks()
            window.exec_()



# Download DXBX Deskotop
    def download_des(self):
        self.pushButton_3.clicked.connect(self.desktop_download)

    def desktop_download(self):
        class GeeksforGeeks(QDialog):
 
            def __init__(self):
                super().__init__()
         
                # calling a defined method to initialize UI
                self.init_UI()
         
            # method for creating UI widgets
            def init_UI(self):
                self.setFixedSize(300, 100)
                self.setWindowIcon(QtGui.QIcon('ico.ico'))
                self.progressBar = QProgressBar(self)
                self.progressBar.setGeometry(25, 45, 210, 30)        
                self.button = QPushButton('Скачать', self)
                self.button.move(220, 45)
                self.button.clicked.connect(self.Download)
                self.setGeometry(310, 310, 280, 170)
                self.setWindowTitle("Download DXBX Desktop")

                self.show()
        #close from xmark
            def closeEvent(self, init_UI):
                GeeksforGeeks.destroy(self)
         
            # when push button is pressed, this method is call
            def Handle_Progress(self, blocknum, blocksize, totalsize):
         
                ## calculate the progress
                readed_data = blocknum * blocksize
         
                if totalsize > 0:
                    download_percentage = readed_data * 100 / totalsize
                    self.progressBar.setValue(download_percentage)
                    QApplication.processEvents()


            # method to download any file using urllib
            def Download(self):
         
                # specify the url of the file which is to be downloaded
                down_url = 'http://updates.dxbx.ru/download/DxBx.Desktop-setup-v1.1.7.exe' # specify download url here
         
                # specify save location where the file is to be saved
                save_loc = 'DxBx.Desktop-setup-v1.1.7.exe'
         
                # Downloading using urllib
                urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)

                GeeksforGeeks.destroy(self)

        if __name__ == '__main__':
            App = QApplication(sys.argv)
            window = GeeksforGeeks()
            window.exec_()


# Download UTM
    def download_utm(self):
        self.pushButton_4.clicked.connect(self.utm_download)

    def utm_download(self):
        class GeeksforGeeks(QDialog):
            def __init__(self):
                super().__init__()
                self.init_UI()
         
            # method for creating UI widgets
            def init_UI(self):
                self.setFixedSize(300, 100)
                self.setWindowIcon(QtGui.QIcon('ico.ico'))
                self.progressBar = QProgressBar(self)
                self.progressBar.setGeometry(25, 45, 210, 30)        
                self.button = QPushButton('Скачать', self)
                self.button.move(220, 45)
                self.button.clicked.connect(self.Download)
                self.setGeometry(310, 310, 280, 170)
                self.setWindowTitle("Download UTM")

                self.show()

        #close from xmark
            def closeEvent(self, init_UI):
                GeeksforGeeks.destroy(self)
         
            # when push button is pressed, this method is called
            def Handle_Progress(self, blocknum, blocksize, totalsize):
         
                ## calculate the progress
                readed_data = blocknum * blocksize
         
                if totalsize > 0:
                    download_percentage = readed_data * 100 / totalsize
                    self.progressBar.setValue(download_percentage)
                    QApplication.processEvents()

            # method to download any file using urllib
            def Download(self):
                # specify the url of the file which is to be downloaded
                down_url = 'http://egais.ru/files/distr/silent-setup-4.2.0-b2463.exe' # specify download url here
         
                # specify save location where the file is to be saved
                save_loc = 'silent-setup-4.2.0-b2463.exe'
         
                # Downloading using urllib
                urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)

                GeeksforGeeks.destroy(self)

        if __name__ == '__main__':
            App = QApplication(sys.argv)
            window = GeeksforGeeks()
            window.exec_()

# move to trasport and config
    def move_to_config(self):
        self.pushButton_7.clicked.connect(self.trans_conf)

    def trans_conf(self):

        try:
            shutil.copy2('transport.properties', 'C:/UTM/transporter/conf')
            ovpn_to_copy = glob.glob('*.ovpn')
            destination = (r'C:/Program Files/OpenVPN/config')
            for file in ovpn_to_copy:
                shutil.copy2(file, destination)
            f = open(r'C:/UTM/transporter/conf/transport.properties')
            f.close()

            message_move = QMessageBox()
            message_move.setWindowIcon(QtGui.QIcon('ico.ico'))
            message_move.setWindowTitle("Конфиг и Transport")
            message_move.setText("Конфиг VPN и Transport успешно перемещены")
            message_move.setIcon(QMessageBox.Information)
            message_move.StandardButton(QMessageBox.Ok)
            message_move.exec_()

        except Exception:
            def error(self):
                print('Файл недоступен')
                message_move = QMessageBox()
                message_move.setWindowIcon(QtGui.QIcon('ico.ico'))
                message_move.setWindowTitle("Конфиг VPN и Transport ERROR")
                message_move.setText("Файлы небыли перемещены, пожалуйста проверьте находятся ли файлы \
                    в текущей папке и попробуйте снова. Или перезапустите программу от имени администратора.")
                message_move.setIcon(QMessageBox.Warning)
                message_move.StandardButton(QMessageBox.Ok)
                message_move.exec_()
            error(self)


# settings firewall and button
    def firewall_button(self):
        self.pushButton_5.clicked.connect(self.settings_firewall)

    def settings_firewall(self):
        os.system('powershell -command "powershell -executionpolicy RemoteSigned -file scene.ps1"')
        Word = ("True")
        if Word in open('output_scene.txt', encoding='UTF-16 LE').read():
            print("word found")
            firewall = QMessageBox()
            firewall.setWindowIcon(QtGui.QIcon('ico.ico'))
            firewall.setWindowTitle("Брандмауэр")
            firewall.setText('Правило было успешно создано.')
            firewall.setIcon(QMessageBox.Information)
            firewall.StandardButton(QMessageBox.Ok)
            firewall.exec_()
        else:
            firewall_error = QMessageBox()
            firewall_error.setWindowIcon(QtGui.QIcon('ico.ico'))
            firewall_error.setWindowTitle("Брандмауэр ERROR")
            firewall_error.setText('Правило не было создано. В файле output_scene.txt описана ошибка.')
            firewall_error.setIcon(QMessageBox.Warning)
            firewall_error.StandardButton(QMessageBox.Ok)
            firewall_error.exec_()
            print("word not found")


# restart service and button
    def service_button(self):
        self.pushButton_6.clicked.connect(self.settings_service)

    def settings_service(self):
        os.system('powershell -command "powershell -executionpolicy RemoteSigned -file scene2.ps1"')
        Word_for_rule = ("CategoryInfo")
        if Word_for_rule in open('output_scene2.txt', encoding='UTF-16 LE').read():
            print("word found")
            service_rule_error = QMessageBox()
            service_rule_error.setWindowIcon(QtGui.QIcon('ico.ico'))
            service_rule_error.setWindowTitle("Перезапуск служб ERROR")
            service_rule_error.setText('Службы небыли перезапущены. В файле output_scene2.txt описана ошибка.')
            service_rule_error.setIcon(QMessageBox.Warning)
            service_rule_error.StandardButton(QMessageBox.Ok)
            service_rule_error.exec_()
        else:
            print("word note found")
            service_rule = QMessageBox()
            service_rule.setWindowIcon(QtGui.QIcon('ico.ico'))
            service_rule.setWindowTitle("Перезапуск служб")
            service_rule.setText('Службы успешно перезапущены.')
            service_rule.setIcon(QMessageBox.Information)
            service_rule.StandardButton(QMessageBox.Ok)
            service_rule.exec_()

# start app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


