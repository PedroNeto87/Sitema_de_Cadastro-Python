# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(727, 564)
        MainWindow.setStyleSheet(u"background-color: rgb(12, 12, 12);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 87 14pt \"Bodoni MT Black\";")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align: left;\n"
"	background-color: rgb(228, 254, 255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(194, 232, 255);\n"
"	text-align: left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(150, 0))
        self.toolBox.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-top-left-radius: 15px;\n"
"}")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setGeometry(QRect(0, 0, 150, 436))
        font = QFont()
        font.setPointSize(8)
        self.page1.setFont(font)
        self.page1.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_5 = QVBoxLayout(self.page1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_pg_home = QPushButton(self.page1)
        self.btn_pg_home.setObjectName(u"btn_pg_home")
        self.btn_pg_home.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_pg_home.setFont(font1)
        self.btn_pg_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_home.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_pg_home)

        self.btn_pg_empresas = QPushButton(self.page1)
        self.btn_pg_empresas.setObjectName(u"btn_pg_empresas")
        self.btn_pg_empresas.setMinimumSize(QSize(0, 30))
        self.btn_pg_empresas.setFont(font1)
        self.btn_pg_empresas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_empresas.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_pg_empresas)

        self.btn_pg_usuarios = QPushButton(self.page1)
        self.btn_pg_usuarios.setObjectName(u"btn_pg_usuarios")
        self.btn_pg_usuarios.setMinimumSize(QSize(0, 30))
        self.btn_pg_usuarios.setFont(font1)
        self.btn_pg_usuarios.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_pg_usuarios)

        self.btn_pg_produtos = QPushButton(self.page1)
        self.btn_pg_produtos.setObjectName(u"btn_pg_produtos")
        self.btn_pg_produtos.setMinimumSize(QSize(0, 30))
        self.btn_pg_produtos.setFont(font1)

        self.verticalLayout_5.addWidget(self.btn_pg_produtos)

        self.btn_pg_contatos = QPushButton(self.page1)
        self.btn_pg_contatos.setObjectName(u"btn_pg_contatos")
        self.btn_pg_contatos.setMinimumSize(QSize(0, 30))
        self.btn_pg_contatos.setFont(font1)
        self.btn_pg_contatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_contatos.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_pg_contatos)

        self.btn_pg_sobre = QPushButton(self.page1)
        self.btn_pg_sobre.setObjectName(u"btn_pg_sobre")
        self.btn_pg_sobre.setMinimumSize(QSize(0, 30))
        self.btn_pg_sobre.setFont(font1)
        self.btn_pg_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_sobre.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_pg_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page1, u"Menu")
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2.setGeometry(QRect(0, 0, 132, 157))
        self.verticalLayout_6 = QVBoxLayout(self.page2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.label_4 = QLabel(self.page2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(12, 12, 12);")

        self.verticalLayout_6.addWidget(self.label_4)

        self.toolBox.addItem(self.page2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 9, 9)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.main_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_8 = QVBoxLayout(self.pg_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_8.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro_empresas = QWidget()
        self.pg_cadastro_empresas.setObjectName(u"pg_cadastro_empresas")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro_empresas)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.pg_cadastro_empresas)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_12 = QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_logradouro = QLineEdit(self.frame_4)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 2, 0, 1, 3)

        self.txt_municipio = QLineEdit(self.frame_4)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 4, 0, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_4)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 5, 0, 1, 1)

        self.txt_numero = QLineEdit(self.frame_4)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 3, 0, 1, 1)

        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 1, 1, 2)

        self.lbl_empresas = QLabel(self.frame_4)
        self.lbl_empresas.setObjectName(u"lbl_empresas")
        self.lbl_empresas.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_empresas.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.gridLayout.addWidget(self.lbl_empresas, 0, 0, 1, 3)

        self.txt_bairro = QLineEdit(self.frame_4)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 3, 2, 1, 1)

        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 5, 1, 1, 2)

        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 1, 0, 1, 1)

        self.txt_uf = QLineEdit(self.frame_4)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 4, 1, 1, 1)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 4, 2, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_4)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 3, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.btn_cadastrar_empresa = QPushButton(self.tab)
        self.btn_cadastrar_empresa.setObjectName(u"btn_cadastrar_empresa")
        self.btn_cadastrar_empresa.setMinimumSize(QSize(160, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.btn_cadastrar_empresa.setFont(font2)
        self.btn_cadastrar_empresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_empresa.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_cadastrar_empresa, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 60))
        self.label_5.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.verticalLayout_11.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_company = QTableWidget(self.tab_2)
        if (self.tb_company.columnCount() < 11):
            self.tb_company.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"}")

        self.horizontalLayout_5.addWidget(self.tb_company)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 11pt \"MS Shell Dig 2\";\n"
"	color: rgb(0, 24, 74);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(230, 230, 230);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_excel_empresa = QPushButton(self.frame_3)
        self.btn_excel_empresa.setObjectName(u"btn_excel_empresa")
        self.btn_excel_empresa.setMinimumSize(QSize(90, 30))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dig 2"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_excel_empresa.setFont(font3)
        self.btn_excel_empresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_empresa.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(49, 147, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_excel_empresa)

        self.btn_alterar_empresa = QPushButton(self.frame_3)
        self.btn_alterar_empresa.setObjectName(u"btn_alterar_empresa")
        self.btn_alterar_empresa.setMinimumSize(QSize(90, 30))
        self.btn_alterar_empresa.setFont(font3)
        self.btn_alterar_empresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_empresa.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_alterar_empresa)

        self.btn_excluir_empresa = QPushButton(self.frame_3)
        self.btn_excluir_empresa.setObjectName(u"btn_excluir_empresa")
        self.btn_excluir_empresa.setMinimumSize(QSize(90, 30))
        self.btn_excluir_empresa.setFont(font3)
        self.btn_excluir_empresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_empresa.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(199, 66, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_excluir_empresa)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastro_empresas)
        self.pg_cadastro_usuarios = QWidget()
        self.pg_cadastro_usuarios.setObjectName(u"pg_cadastro_usuarios")
        self.verticalLayout_15 = QVBoxLayout(self.pg_cadastro_usuarios)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabWidget_2 = QTabWidget(self.pg_cadastro_usuarios)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_usuarios = QLabel(self.frame_5)
        self.lbl_usuarios.setObjectName(u"lbl_usuarios")
        self.lbl_usuarios.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_usuarios.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.gridLayout_2.addWidget(self.lbl_usuarios, 0, 0, 1, 2)

        self.lbl_nome = QLabel(self.frame_5)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lbl_nome, 1, 0, 1, 1)

        self.txt_nomeUsuario = QLineEdit(self.frame_5)
        self.txt_nomeUsuario.setObjectName(u"txt_nomeUsuario")
        self.txt_nomeUsuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.txt_nomeUsuario, 1, 1, 1, 1)

        self.lbl_usuario = QLabel(self.frame_5)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lbl_usuario, 2, 0, 1, 1)

        self.txt_usuario = QLineEdit(self.frame_5)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.txt_usuario, 2, 1, 1, 1)

        self.lbl_senha = QLabel(self.frame_5)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lbl_senha, 3, 0, 1, 1)

        self.txt_senha = QLineEdit(self.frame_5)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.txt_senha, 3, 1, 1, 1)

        self.lbl_repeteSenha = QLabel(self.frame_5)
        self.lbl_repeteSenha.setObjectName(u"lbl_repeteSenha")
        self.lbl_repeteSenha.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lbl_repeteSenha, 4, 0, 1, 1)

        self.txt_repeteSenha = QLineEdit(self.frame_5)
        self.txt_repeteSenha.setObjectName(u"txt_repeteSenha")
        self.txt_repeteSenha.setEchoMode(QLineEdit.Password)
        self.txt_repeteSenha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.txt_repeteSenha, 4, 1, 1, 1)

        self.lbl_perfil = QLabel(self.frame_5)
        self.lbl_perfil.setObjectName(u"lbl_perfil")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_perfil.sizePolicy().hasHeightForWidth())
        self.lbl_perfil.setSizePolicy(sizePolicy1)
        self.lbl_perfil.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lbl_perfil, 5, 0, 1, 1)

        self.cb_perfil = QComboBox(self.frame_5)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.cb_perfil, 5, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.btn_cadastrar_usuario = QPushButton(self.tab_3)
        self.btn_cadastrar_usuario.setObjectName(u"btn_cadastrar_usuario")
        self.btn_cadastrar_usuario.setMinimumSize(QSize(160, 30))
        self.btn_cadastrar_usuario.setFont(font2)
        self.btn_cadastrar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_usuario.setLayoutDirection(Qt.LeftToRight)
        self.btn_cadastrar_usuario.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_cadastrar_usuario, 0, Qt.AlignHCenter)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_18 = QVBoxLayout(self.tab_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 60))
        self.label_6.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.verticalLayout_18.addWidget(self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tb_users = QTableWidget(self.tab_4)
        if (self.tb_users.columnCount() < 5):
            self.tb_users.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_users.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_users.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_users.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_users.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_users.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tb_users.setObjectName(u"tb_users")
        self.tb_users.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"}")

        self.horizontalLayout_6.addWidget(self.tb_users)

        self.frame_6 = QFrame(self.tab_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 11pt \"MS Shell Dig 2\";\n"
"	color: rgb(0, 24, 74);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(230, 230, 230);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btn_excel_usuario = QPushButton(self.frame_6)
        self.btn_excel_usuario.setObjectName(u"btn_excel_usuario")
        self.btn_excel_usuario.setMinimumSize(QSize(90, 30))
        self.btn_excel_usuario.setFont(font3)
        self.btn_excel_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_usuario.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(49, 147, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_17.addWidget(self.btn_excel_usuario)

        self.btn_alterar_usuario = QPushButton(self.frame_6)
        self.btn_alterar_usuario.setObjectName(u"btn_alterar_usuario")
        self.btn_alterar_usuario.setMinimumSize(QSize(90, 30))
        self.btn_alterar_usuario.setFont(font3)
        self.btn_alterar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_usuario.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_17.addWidget(self.btn_alterar_usuario)

        self.btn_excluir_usuario = QPushButton(self.frame_6)
        self.btn_excluir_usuario.setObjectName(u"btn_excluir_usuario")
        self.btn_excluir_usuario.setMinimumSize(QSize(90, 30))
        self.btn_excluir_usuario.setFont(font3)
        self.btn_excluir_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_usuario.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(199, 66, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_17.addWidget(self.btn_excluir_usuario)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addWidget(self.frame_6)


        self.verticalLayout_18.addLayout(self.horizontalLayout_6)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_15.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pg_cadastro_usuarios)
        self.pg_cadastro_produtos = QWidget()
        self.pg_cadastro_produtos.setObjectName(u"pg_cadastro_produtos")
        self.verticalLayout_20 = QVBoxLayout(self.pg_cadastro_produtos)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tabWidget_3 = QTabWidget(self.pg_cadastro_produtos)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_21 = QVBoxLayout(self.tab_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_7 = QFrame(self.tab_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 3)

        self.lbl_descricao = QLabel(self.frame_7)
        self.lbl_descricao.setObjectName(u"lbl_descricao")
        self.lbl_descricao.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.lbl_descricao, 1, 0, 1, 2)

        self.txt_descricao = QLineEdit(self.frame_7)
        self.txt_descricao.setObjectName(u"txt_descricao")

        self.gridLayout_3.addWidget(self.txt_descricao, 1, 2, 1, 1)

        self.lbl_unidade = QLabel(self.frame_7)
        self.lbl_unidade.setObjectName(u"lbl_unidade")
        self.lbl_unidade.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.lbl_unidade, 2, 0, 1, 2)

        self.txt_unidade = QLineEdit(self.frame_7)
        self.txt_unidade.setObjectName(u"txt_unidade")

        self.gridLayout_3.addWidget(self.txt_unidade, 2, 2, 1, 1)

        self.lbl_preco = QLabel(self.frame_7)
        self.lbl_preco.setObjectName(u"lbl_preco")
        self.lbl_preco.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.lbl_preco, 3, 0, 1, 1)

        self.txt_preco = QLineEdit(self.frame_7)
        self.txt_preco.setObjectName(u"txt_preco")

        self.gridLayout_3.addWidget(self.txt_preco, 3, 1, 1, 2)

        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_15, 4, 0, 1, 2)

        self.txt_estoque = QLineEdit(self.frame_7)
        self.txt_estoque.setObjectName(u"txt_estoque")

        self.gridLayout_3.addWidget(self.txt_estoque, 4, 2, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_7)

        self.btn_cadastra_produto = QPushButton(self.tab_5)
        self.btn_cadastra_produto.setObjectName(u"btn_cadastra_produto")
        self.btn_cadastra_produto.setMinimumSize(QSize(160, 30))
        self.btn_cadastra_produto.setFont(font2)
        self.btn_cadastra_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastra_produto.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_cadastra_produto, 0, Qt.AlignHCenter)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_23 = QVBoxLayout(self.tab_6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_16 = QLabel(self.tab_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 60))
        self.label_16.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.verticalLayout_23.addWidget(self.label_16)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tb_product = QTableWidget(self.tab_6)
        if (self.tb_product.columnCount() < 5):
            self.tb_product.setColumnCount(5)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_product.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_product.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_product.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_product.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_product.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        self.tb_product.setObjectName(u"tb_product")
        self.tb_product.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"}")

        self.horizontalLayout_7.addWidget(self.tb_product)

        self.frame_8 = QFrame(self.tab_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 11pt \"MS Shell Dig 2\";\n"
"	color: rgb(0, 24, 74);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(230, 230, 230);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btn_excel_produto = QPushButton(self.frame_8)
        self.btn_excel_produto.setObjectName(u"btn_excel_produto")
        self.btn_excel_produto.setMinimumSize(QSize(90, 30))
        self.btn_excel_produto.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(49, 147, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_22.addWidget(self.btn_excel_produto)

        self.btn_alterar_produto = QPushButton(self.frame_8)
        self.btn_alterar_produto.setObjectName(u"btn_alterar_produto")
        self.btn_alterar_produto.setMinimumSize(QSize(90, 30))
        self.btn_alterar_produto.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_22.addWidget(self.btn_alterar_produto)

        self.btn_excluir_produto = QPushButton(self.frame_8)
        self.btn_excluir_produto.setObjectName(u"btn_excluir_produto")
        self.btn_excluir_produto.setMinimumSize(QSize(90, 30))
        self.btn_excluir_produto.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(199, 66, 0);\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_22.addWidget(self.btn_excluir_produto)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_4)


        self.horizontalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_23.addLayout(self.horizontalLayout_7)

        self.tabWidget_3.addTab(self.tab_6, "")

        self.verticalLayout_20.addWidget(self.tabWidget_3)

        self.Pages.addWidget(self.pg_cadastro_produtos)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_14 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.pg_contatos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")

        self.verticalLayout_14.addWidget(self.label_11)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, -1, 100)
        self.label_7 = QLabel(self.pg_contatos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_13.addWidget(self.label_7)

        self.label_8 = QLabel(self.pg_contatos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_13.addWidget(self.label_8)

        self.lbl_github = QLabel(self.pg_contatos)
        self.lbl_github.setObjectName(u"lbl_github")
        self.lbl_github.setMaximumSize(QSize(16777215, 20))
        self.lbl_github.setOpenExternalLinks(True)

        self.verticalLayout_13.addWidget(self.lbl_github)

        self.lbl_linkedin = QLabel(self.pg_contatos)
        self.lbl_linkedin.setObjectName(u"lbl_linkedin")
        self.lbl_linkedin.setMaximumSize(QSize(16777215, 20))
        self.lbl_linkedin.setOpenExternalLinks(True)

        self.verticalLayout_13.addWidget(self.lbl_linkedin)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_16 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_12 = QLabel(self.pg_sobre)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")

        self.verticalLayout_16.addWidget(self.label_12)

        self.label_13 = QLabel(self.pg_sobre)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_13)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_19.addWidget(self.Pages)


        self.verticalLayout_2.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Pedro Neto</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.page1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.page1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_pg_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_pg_empresas.setText(QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.btn_pg_usuarios.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.btn_pg_produtos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.btn_pg_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_pg_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page1), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Sistema de Cadastros</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-weight:600;\">Status:</span> Ativo</p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-weight:600;\">Venc:</span> 31/12/2999</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600;\">Sistema de Cadastros</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo.png\"/></p></body></html>", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logardouro", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.lbl_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/empresa.png\"/><span style=\" font-size:48pt; font-weight:600; vertical-align:super;\">EMPRESAS</span></p></body></html>", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.btn_cadastrar_empresa.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">EMPRESAS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_excel_empresa.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_empresa.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_empresa.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.lbl_usuarios.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/usuario.png\"/><span style=\" font-size:48pt; font-weight:600; vertical-align:super;\">USU\u00c1RIOS</span></p></body></html>", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.txt_nomeUsuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome completo", None))
        self.lbl_usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.lbl_repeteSenha.setText(QCoreApplication.translate("MainWindow", u"Repete senha:", None))
        self.txt_repeteSenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repete senha", None))
        self.lbl_perfil.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.btn_cadastrar_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">USU\u00c1RIOS</span></p></body></html>", None))
        ___qtablewidgetitem11 = self.tb_users.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tb_users.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem13 = self.tb_users.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None));
        ___qtablewidgetitem14 = self.tb_users.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"SENHA", None));
        ___qtablewidgetitem15 = self.tb_users.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"PERFIL", None));
        self.btn_excel_usuario.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_usuario.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_usuario.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/produto.png\"/><span style=\" font-size:48pt; font-weight:600; vertical-align:super;\">PRODUTOS</span></p></body></html>", None))
        self.lbl_descricao.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o:", None))
        self.txt_descricao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do produto", None))
        self.lbl_unidade.setText(QCoreApplication.translate("MainWindow", u"Unidade:", None))
        self.txt_unidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unidade do produto", None))
        self.lbl_preco.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o:", None))
        self.txt_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o do produto", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Estoque:", None))
        self.txt_estoque.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estoque do produto", None))
        self.btn_cadastra_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">PRODUTOS</span></p></body></html>", None))
        ___qtablewidgetitem16 = self.tb_product.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"C\u00d3DIGO", None));
        ___qtablewidgetitem17 = self.tb_product.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem18 = self.tb_product.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"UNIDADE", None));
        ___qtablewidgetitem19 = self.tb_product.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O", None));
        ___qtablewidgetitem20 = self.tb_product.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None));
        self.btn_excel_produto.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_produto.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_produto.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/contato.png\"/><span style=\" font-size:48pt; font-weight:600; vertical-align:super;\">Contatos</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; vertical-align:super;\">(31)99398-8562</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; vertical-align:super;\">pedrofcn01@hotmail.com</span></p></body></html>", None))
        self.lbl_github.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/PedroNeto87\"><span style=\" font-size:20pt; text-decoration: underline; color:#ffffff; vertical-align:super;\">https://github.com/PedroNeto87</span></a></p></body></html>", None))
        self.lbl_linkedin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/pedro-ferreira-cunha-neto/\"><span style=\" font-size:20pt; text-decoration: underline; color:#ffffff; vertical-align:super;\">https://www.linkedin.com/in/pedro-ferreira-cunha-neto/</span></a></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/sobre.png\"/><span style=\" font-size:48pt; font-weight:600; vertical-align:super;\">Sobre</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Este sistema realiza cadastro de empresas com base na consulta do CNPJ utilizando API da Receita Federal, faz tamb\u00e9m cadastro de usu\u00e1rios e produtos e armazena em um banco de dados SQLITE3.</span></p><p><span style=\" font-size:14pt;\">Tamb\u00e9m gera arquivo em formato .XLSX(Excel) com as informa\u00e7\u00f5es cadastradas no sistema.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt;\">\u00a9 Pedro_Neto 2023</span></p></body></html>", None))
    # retranslateUi

