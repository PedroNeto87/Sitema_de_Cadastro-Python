import sys
import pandas as pd
import sqlite3
import os
from PySide6 import QtCore 
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
from ui_functions import consulta_cnpj
from database import Data_base


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Cadastro')
        appIcon = QIcon(u'icons/logo4.png')
        self.setWindowIcon(appIcon)

        ##############################################
        #TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.menuAnimado)
        #################################################
        #PAGINAS DO SISTEMA
        self.btn_pg_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_empresas))
        self.btn_pg_usuarios.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_usuarios))
        self.btn_pg_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        self.btn_pg_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        ####################################################################################################
        #PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ
        self.txt_cnpj.editingFinished.connect(self.consultar_api)
        #########################################################
        #CADASTRAR EMPRESA
        self.btn_cadastrar_empresa.clicked.connect(self.cadastrar_empresa)
        ##################################################################
        #ATUALIZAR CADASTRO DE EMPRESAS
        self.btn_alterar_empresa.clicked.connect(self.editar_empresas)
        ######################################################
        #EXCLUIR CADASTRO DE EMPRESAS
        self.btn_excluir_empresa.clicked.connect(self.excluir_empresa)
        ##############################################################
        #GERAR ARQUIVO EXCEL DE EMPRESAS
        #self.btn_excel_empresa.clicked.connect(self.gerar_excel_interface)
        self.btn_excel_empresa.clicked.connect(self.gerar_excel_banco)
        ##################################################################
        #PREENCHER A TABELA DE EMPRESAS
        self.tabela_empresas()
        ######################

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
            self.tabela_empresas()
            self.txt_cnpj.setText(''), self.txt_nome.setText(''), self.txt_logradouro.setText(''), self.txt_numero.setText(''), self.txt_complemento.setText(''), self.txt_bairro.setText(''), self.txt_municipio.setText(''), self.txt_uf.setText(''), self.txt_cep.setText(''), self.txt_telefone.setText(''), self.txt_email.setText('')
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Erro')
            msg.setText('Erro ao cadastrar, verifique se as informações foram preenchidas corretamente')
            msg.exec()
            db.close_connection()

    def tabela_empresas(self):
        db = Data_base()
        db.connect()
        resultado = db.select_all_campanies()

        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(resultado))

        for linha, texto in enumerate(resultado):
            for coluna, dado in enumerate(texto):
                self.tb_company.setItem(linha, coluna, QTableWidgetItem(str(dado)))
        db.close_connection()

    def editar_empresas(self):
        dados = []
        atualizar_dados = []

        for linha in range(self.tb_company.rowCount()):
            for coluna in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(linha, coluna).text())
            
            atualizar_dados.append(dados)
            dados = []

        #ATUALIZAR DADOS NO BANCO
        db = Data_base()
        db.connect()

        for emp in atualizar_dados:
            db.update_company(tuple(emp))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Atualização de Dados')
        msg.setText('Dados atualizados com sucesso!')
        msg.exec()

    def excluir_empresa(self):
        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle('Excluir')
        msg.setText('Este registro será excluído')
        msg.setInformativeText('Você tem certeza que deseja excluir?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_company(cnpj)
            self.tabela_empresas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Empresas')
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def gerar_excel_interface(self):
        #pip install openpyxl
        #pip install pandas
        dados = []
        todos_dados = []

        for linha in range(self.tb_company.rowCount()):
            for coluna in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(linha, coluna).text())
            todos_dados.append(dados)
            dados = []

        colunas = ['CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL']
        empresas = pd.DataFrame(todos_dados, columns=colunas)
        caminho_arquivo = os.path.expanduser('~/Desktop/Empresas.xlsx')
        empresas.to_excel(caminho_arquivo, sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Excel')
        msg.setText('Relatório Excel gerado com sucesso!')
        msg.exec()

    def gerar_excel_banco(self):
        #pip install openpyxl
        #pip install pandas
        #import sqlite3
        cnx = sqlite3.connect('system.db')
        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", cnx)
        caminho_arquivo = os.path.expanduser('~/Desktop/Empresas.xlsx')
        empresas.to_excel(caminho_arquivo, sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Excel')
        msg.setText('Relatório Excel gerado com sucesso!')
        msg.exec()



if __name__ == '__main__':
    db = Data_base()
    db.connect()
    db.create_table_companies()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
