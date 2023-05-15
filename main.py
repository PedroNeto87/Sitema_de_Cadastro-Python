import sys
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from ui_main import Ui_MainWindow
from ui_functions import consulta_cnpj
from database import Data_base


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Cadastro')
        appIcon = QIcon(u'')
        self.setWindowIcon(appIcon)

        ##############################################
        #TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.menuAnimado)
        ##############################################
        #PAGINAS DO SISTEMA
        self.btn_pg_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_empresa))
        self.btn_pg_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        self.btn_pg_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        ###########################################################################################
        #PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ
        self.txt_cnpj.editingFinished.connect(self.consultar_api)
        ######################################################
        #CADASTRAR EMPRESA
        self.btn_cadastrar_empresa.clicked.connect(self.cadastrar_empresa)

    def menuAnimado(self):
        width = self.left_menu.width()
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consultar_api(self):
        campos = consulta_cnpj(self.txt_cnpj.text())

        self.txt_nome.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_numero.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_municipio.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7].replace('.', '').replace('-', ''))
        self.txt_telefone.setText(campos[8].replace('(', '').replace('-', '').replace(')', ''))
        self.txt_email.setText(campos[9])

    def cadastrar_empresa(self):
        db = Data_base()
        db.connect()
        
        fulDataSet = (self.txt_cnpj.text(), self.txt_nome.text(), self.txt_logradouro.text(), self.txt_numero.text(), self.txt_complemento.text(), self.txt_bairro.text(), self.txt_municipio.text(), self.txt_uf.text(), self.txt_cep.text(), self.txt_telefone.text().strip(), self.txt_email.text())

        #Cadastrar no banco de dados
        resp = db.register_company(fulDataSet)
        if resp == 'OK':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro realizado')
            msg.setText('Cadastro realizado com sucesso!')
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Erro')
            msg.setText('Erro ao cadastrar, verifique se as informações foram preenchidas corretamente')
            msg.exec()
            db.close_connection()



if __name__ == '__main__':
    db = Data_base()
    db.connect()
    db.create_table_companies()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
