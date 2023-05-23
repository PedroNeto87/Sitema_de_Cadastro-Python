import sys
import pandas as pd
import sqlite3
import os
from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from ui_functions import consultaCnpj
from database import DataBase


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema')
        appIcon = QIcon(u'icons/logo.png')
        self.setWindowIcon(appIcon)
        self.setFixedSize(QSize(431, 452))
        

        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        self.user = DataBase()
        self.user.connect()
        autenticado = self.user.checkUser(self.txt_user.text().upper(), self.txt_password.text())

        if autenticado == 'Administrador' or autenticado == 'Usuario':
            self.w = MainWindow(autenticado)
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Erro ao acessar')
                msg.setText(f'Login ou senha incorretos\n\nTentativa: {self.tentativas +1} de 3')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                self.user.closeConnection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Cadastros')
        appIcon = QIcon(u'icons/logo.png')
        self.setWindowIcon(appIcon)

        #CHECAGEM DE USUARIO
        if user == 'Usuario':
            self.btn_pg_usuarios.setVisible(False)

        #TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.menuAnimado)

        #PAGINAS DO SISTEMA
        self.btn_pg_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_pg_empresas.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_empresas))
        self.btn_pg_usuarios.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_usuarios))
        self.btn_pg_produtos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_produtos))
        self.btn_pg_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        self.btn_pg_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))

        #PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ
        self.txt_cnpj.editingFinished.connect(self.consultarApi)

        #CADASTRAR EMPRESA, USUARIO, PRODUTO
        self.btn_cadastrar_empresa.clicked.connect(self.cadastrarEmpresa)
        self.btn_cadastrar_usuario.clicked.connect(self.cadastrarUsuario)
        self.btn_cadastra_produto.clicked.connect(self.cadastrarProduto)

        #ATUALIZAR CADASTRO EMPRESAS, USUARIOS, PRODUTOS
        self.btn_alterar_empresa.clicked.connect(self.editarEmpresas)
        self.btn_alterar_usuario.clicked.connect(self.editarUsuarios)
        self.btn_alterar_produto.clicked.connect(self.editarProdutos)

        #EXCLUIR CADASTRO EMPRESAS, USUARIOS, PRODUTOS
        self.btn_excluir_empresa.clicked.connect(self.excluirEmpresa)
        self.btn_excluir_usuario.clicked.connect(self.excluirUsuarios)
        self.btn_excluir_produto.clicked.connect(self.excluirProdutos)

        #GERAR ARQUIVO EXCEL EMPRESAS, USUARIOS, PRODUTOS
        self.btn_excel_empresa.clicked.connect(self.excelEmpresas)
        self.btn_excel_usuario.clicked.connect(self.excelUsuarios)
        self.btn_excel_produto.clicked.connect(self.excelProdutos)

        #PREENCHER TABELA EMPRESAS, USUÁRIOS, PRODUTOS
        self.tabelaEmpresas()
        self.tabelaUsuarios()
        self.tabelaProdutos()

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

    def cadastrarUsuario(self):
        if self.txt_senha.text() != self.txt_repeteSenha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Senhas divergentes')
            msg.setText('As senhas devem ser iguais!')
            msg.exec()
            return None
        
        nome = self.txt_nomeUsuario.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.connect()
        db.insertUser(nome, user, password, access)
        db.closeConnection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Cadastro de usuário')
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

        self.txt_nomeUsuario.setText('')
        self.txt_usuario.setText('')
        self.txt_senha.setText('')
        self.txt_repeteSenha.setText('')
        self.tabelaUsuarios()

    def tabelaUsuarios(self):
        db = DataBase()
        db.connect()
        resultado = db.selecAllUsers()
        self.tb_users.clearContents()
        self.tb_users.setRowCount(len(resultado))

        for linha, texto in enumerate(resultado):
            for coluna, dado in enumerate(texto):
                self.tb_users.setItem(linha, coluna, QTableWidgetItem(str(dado)))

        db.closeConnection()

    def editarUsuarios(self):
        dados = []
        atualizarDados = []

        for linha in range(self.tb_users.rowCount()):
            for coluna in range(self.tb_users.columnCount()):
                dados.append(self.tb_users.item(linha, coluna).text())
            atualizarDados.append(dados)
            dados = []
        
        db = DataBase()
        db.connect()
        for user in atualizarDados:
            db.updateUser(tuple(user)) 
        db.closeConnection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Atualização de Dados')
        msg.setText('Dados atualizados com sucesso!')
        msg.exec()

    def excluirUsuarios(self):
        db = DataBase()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle('Excluir')
        msg.setText('Este registro será excluído')
        msg.setInformativeText('Você tem certeza que deseja excluir?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.tb_users.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.deleteUser(id)
            self.tabelaUsuarios()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Usuários')
            msg.setText(resultado)
            msg.exec()

        db.closeConnection()

    def excelUsuarios(self):
        cnx = sqlite3.connect('system.db')
        usuarios = pd.read_sql_query("""SELECT * FROM Usuarios""", cnx)
        caminhoArquivo = os.path.expanduser('~/Desktop/Usuarios.xlsx')
        usuarios.to_excel(caminhoArquivo, sheet_name='usuarios', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Excel')
        msg.setText('Relatório Excel gerado com sucesso!')
        msg.exec()

    def consultarApi(self):
        campos = consultaCnpj(self.txt_cnpj.text())

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

    def cadastrarEmpresa(self):
        db = DataBase()
        db.connect()
        
        fulDataSet = (self.txt_cnpj.text(), self.txt_nome.text(), self.txt_logradouro.text(), self.txt_numero.text(), self.txt_complemento.text(), self.txt_bairro.text(), self.txt_municipio.text(), self.txt_uf.text(), self.txt_cep.text(), self.txt_telefone.text().strip(), self.txt_email.text())

        resp = db.insertCompany(fulDataSet)
        if resp == 'OK':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro realizado')
            msg.setText('Cadastro realizado com sucesso!')
            msg.exec()
            self.tabelaEmpresas()
            self.txt_cnpj.setText(''), self.txt_nome.setText(''), self.txt_logradouro.setText(''), self.txt_numero.setText(''), self.txt_complemento.setText(''), self.txt_bairro.setText(''), self.txt_municipio.setText(''), self.txt_uf.setText(''), self.txt_cep.setText(''), self.txt_telefone.setText(''), self.txt_email.setText('')
            db.closeConnection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Erro')
            msg.setText('Erro ao cadastrar, verifique se as informações foram preenchidas corretamente')
            msg.exec()
            db.closeConnection()

    def tabelaEmpresas(self):
        db = DataBase()
        db.connect()
        resultado = db.selectAllCampanies()
        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(resultado))

        for linha, texto in enumerate(resultado):
            for coluna, dado in enumerate(texto):
                self.tb_company.setItem(linha, coluna, QTableWidgetItem(str(dado)))

        db.closeConnection()

    def editarEmpresas(self):
        dados = []
        atualizarDados = []
        for linha in range(self.tb_company.rowCount()):
            for coluna in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(linha, coluna).text())
            
            atualizarDados.append(dados)
            dados = []

        db = DataBase()
        db.connect()
        for emp in atualizarDados:
            db.updateCompany(tuple(emp))
        db.closeConnection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Atualização de Dados')
        msg.setText('Dados atualizados com sucesso!')
        msg.exec()

    def excluirEmpresa(self):
        db = DataBase()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle('Excluir')
        msg.setText('Este registro será excluído')
        msg.setInformativeText('Você tem certeza que deseja excluir?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.deleteCompany(cnpj)
            self.tabelaEmpresas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Empresas')
            msg.setText(resultado)
            msg.exec()

        db.closeConnection()

    def excelEmpresas(self):
        cnx = sqlite3.connect('system.db')
        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", cnx)
        caminhoArquivo = os.path.expanduser('~/Desktop/Empresas.xlsx')
        empresas.to_excel(caminhoArquivo, sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Excel')
        msg.setText('Relatório Excel gerado com sucesso!')
        msg.exec()

    def gerarExcelInterface(self):
            dados = []
            todosDados = []

            for linha in range(self.tb_company.rowCount()):
                for coluna in range(self.tb_company.columnCount()):
                    dados.append(self.tb_company.item(linha, coluna).text())
                todosDados.append(dados)
                dados = []

            colunas = ['CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL']
            empresas = pd.DataFrame(todosDados, columns=colunas)
            caminhoArquivo = os.path.expanduser('~/Desktop/Empresas.xlsx')
            empresas.to_excel(caminhoArquivo, sheet_name='empresas', index=False)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Excel')
            msg.setText('Relatório Excel gerado com sucesso!')
            msg.exec()

    def cadastrarProduto(self):
        descricao = self.txt_descricao.text()
        unidade = self.txt_unidade.text()
        preco = self.txt_preco.text()
        estoque = self.txt_estoque.text()

        db = DataBase()
        db.connect()
        db.insertProdutct(descricao, unidade, preco, estoque)
        db.closeConnection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Cadastro de Produto')
        msg.setText('Produto cadastrado com sucesso!')
        msg.exec()

        self.txt_descricao.setText('')
        self.txt_unidade.setText('')
        self.txt_preco.setText('')
        self.txt_estoque.setText('')
        self.tabelaProdutos()

    def tabelaProdutos(self):
        db = DataBase()
        db.connect()
        resultado = db.selectAllProducts()
        self.tb_product.clearContents()
        self.tb_product.setRowCount(len(resultado))

        for linha, texto in enumerate(resultado):
            for coluna, dado in enumerate(texto):
                self.tb_product.setItem(linha, coluna, QTableWidgetItem(str(dado)))

        db.closeConnection()

    def editarProdutos(self):
        dados = []
        atualizarDados = []

        for linha in range(self.tb_product.rowCount()):
            for coluna in range(self.tb_product.columnCount()):
                dados.append(self.tb_product.item(linha, coluna).text())
            atualizarDados.append(dados)
            dados = []

        db = DataBase()
        db.connect()
        for produto in atualizarDados:
            db.updateProduct(tuple(produto))
        db.closeConnection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Atualização de Dados')
        msg.setText('Dados atualizados com sucesso!')
        msg.exec()

    def excluirProdutos(self):
        db = DataBase()
        db.connect()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Excluir')
        msg.setText('Este registro será excluído')
        msg.setInformativeText('Você tem certeza que deseja excluir?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.tb_product.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.deleteProduct(codigo)
            self.tabelaProdutos()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Produtos')
            msg.setText(resultado)
            msg.exec()

        db.closeConnection()

    def excelProdutos(self):
        cnx = sqlite3.connect('system.db')
        produtos = pd.read_sql_query("""SELECT * FROM Produtos""", cnx)
        caminhoArquivo = os.path.expanduser('~/Desktop/Produtos.xlsx')
        produtos.to_excel(caminhoArquivo, sheet_name='produtos', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Excel')
        msg.setText('Relatório excel gerado com sucesso!')
        msg.exec()


if __name__ == '__main__':
    db = DataBase()
    db.connect()
    db.createTableUsers()
    db.createTableCompanies()
    db.createTableProducts()
    db.closeConnection()

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
