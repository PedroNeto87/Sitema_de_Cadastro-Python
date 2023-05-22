import sqlite3


class DataBase:
    def __init__(self, name = 'system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def closeConnection(self):
        try:
            self.connection.close()
        except:
            pass

    def createTableUsers(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Usuarios (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NAME TEXT NOT NULL,
                USER TEXT UNIQUE NOT NULL,
                PASSWORD TEXT NOT NULL,
                ACCESS TEXT NOT NULL
                );
            """)
        except AttributeError:
            print('Faça a conexão')

    def insertUser(self, name, user, password, access):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""INSERT INTO Usuarios (name, user, password, access) VALUES (?,?,?,?)""", (name, user, password, access))
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')

    def selecAllUsers(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT * FROM Usuarios ORDER BY ID""")
            usuarios = cursor.fetchall()
            return usuarios
        except AttributeError:
            print('Faça a conexão')

    def updateUser(self, fullDataSet):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""UPDATE Usuarios SET
                ID = '{fullDataSet[0]}',
                NAME = '{fullDataSet[1]}',
                USER = '{fullDataSet[2]}',
                PASSWORD = '{fullDataSet[3]}',
                ACCESS = '{fullDataSet[4]}'

                WHERE ID = '{fullDataSet[0]}'
            """)
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')

    def deleteUser(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""DELETE FROM Usuarios WHERE ID = {id}""")
            self.connection.commit()
            return ("Cadastro de usuário excluído com sucesso!")
        except:
            return("Erro ao excluir registro!")

    def checkUser(self, user, password):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT * FROM Usuarios""")

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == 'Administrador':
                    return 'Administrador'
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == 'Usuário':
                    return 'Usuario'
                else:
                    continue
            return 'Sem acesso'    
        except AttributeError:
            print('Faça a conexão')

    def createTableCompanies(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Empresas (
                CNPJ TEXT,
                NOME TEXT,
                LOGRADOURO TEXT,
                NUMERO TEXT,
                COMPLEMENTO TEXT,
                BAIRRO TEXT,
                MUNICIPIO TEXT,
                UF TEXT,
                CEP TEXT,
                TELEFONE TEXT,
                EMAIL TEXT,
                PRIMARY KEY(CNPJ)
                );
            """)
        except AttributeError:
            print('Faça a conexão')

    def insertCompany(self, fullDataSet):
        camposTabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        qntd = ('?,?,?,?,?,?,?,?,?,?,?')

        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""INSERT INTO Empresas {camposTabela} VALUES ({qntd})""", fullDataSet)
            self.connection.commit()
            return ("OK")
        except:
            return ("Erro")

    def selectAllCampanies(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT * FROM Empresas ORDER BY NOME""")
            empresas = cursor.fetchall()
            return empresas
        except AttributeError:
            print('Faça a conexão')

    def updateCompany(self, fullDataSet):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""UPDATE Empresas SET
                CNPJ = '{fullDataSet[0]}',
                NOME = '{fullDataSet[1]}',
                LOGRADOURO = '{fullDataSet[2]}',
                NUMERO = '{fullDataSet[3]}',
                COMPLEMENTO = '{fullDataSet[4]}',
                BAIRRO = '{fullDataSet[5]}',
                MUNICIPIO = '{fullDataSet[6]}',
                UF = '{fullDataSet[7]}',
                CEP = '{fullDataSet[8]}',
                TELEFONE = '{fullDataSet[9]}',
                EMAIL = '{fullDataSet[10]}'
                
                WHERE CNPJ = '{fullDataSet[0]}'
                """)
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')

    def deleteCompany(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""DELETE FROM Empresas WHERE CNPJ = '{id}'""")
            self.connection.commit()
            return ("Cadastro de empresa excluído com sucesso!")
        except:
            return ("Erro ao excluir registro!")

    def createTableProducts(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS Produtos (
                CODIGO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                DESCRICAO TEXT NOT NULL,
                UNIDADE TEXT NOT NULL,
                PRECO TEXT NOT NULL,
                ESTOQUE TEXT NOT NULL
                );
            """)
        except AttributeError:
            print('Faça a conexão')

    def insertProdutct(self, descricao, unidade, preco, estoque):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""INSERT INTO Produtos (descricao, unidade, preco, estoque) VALUES (?,?,?,?)""", (descricao, unidade, preco, estoque))
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')
    
    def selectAllProducts(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT * FROM Produtos ORDER BY CODIGO""")
            produtos = cursor.fetchall()
            return produtos
        except AttributeError:
            print('Faça a conexão')

    def updateProduct(self, fullDataSet):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""UPDATE Produtos SET
                CODIGO = '{fullDataSet[0]}',
                DESCRICAO = '{fullDataSet[1]}',
                UNIDADE = '{fullDataSet[2]}',
                PRECO = '{fullDataSet[3]}',
                ESTOQUE = '{fullDataSet[4]}'

                WHERE ID = '{fullDataSet[0]}'
            """)
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')
    
    def deleteProduct(self, codigo):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""DELETE FROM Produtos WHERE CODIGO = '{codigo}'""")
            self.connection.commit()
            return("Cadastro de produto excluído com sucesso!")
        except:
            return("Erro ao excluir regsitro!")
