import sqlite3


class Data_base:
    def __init__(self, name = 'system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_companies(self):
        cursor = self.connection.cursor()
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

    def register_company(self, fullDataSet):
        campos_tabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        qntd = ('?,?,?,?,?,?,?,?,?,?,?')

        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela} VALUES ({qntd})""", fullDataSet)
            return ("OK")
        except:
            return ("Erro")
        
    def select_all_campanies(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT * FROM Empresas ORDER BY NOME""")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass

    def delete_company(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""DELETE FROM Empresas WHERE CNPJ = '{id}'""")
            self.connection.commit()
            return ("Cadastro realizado com sucesso!")
        except:
            return ("Erro a excluir registro!")
    
    def update_company(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Empresas SET
            CNPJ = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            NUMERO = '{fullDataSet[3]}',
            COMPLEMENTO = '{fullDataSet[4]}',
            BAIRRO = '{fullDataSet[5]}',
            MUNICIPIO = '{fullDataSet[6]}',
            UP = '{fullDataSet[7]}',
            CEP = '{fullDataSet[8]}',
            TELEFONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}',
            WHERE CNPJ = '{fullDataSet[0]}'
            """)
        self.connection.commit()
