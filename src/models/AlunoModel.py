import sqlite3
from config.db_config import DB_PATH

class AlunoModel:
    def __init__(self, cpf, nome, data_de_nascimento, email, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_de_nascimento = data_de_nascimento
        self.__email = email
        self.__endereco = endereco

    def __str__(self):
        return str(f"'cpf': {self.__cpf}\n'nome': {self.__nome}\ndata_de_nascimento: {self.__data_de_nascimento}\nemail: {self.__email}\nendereco: {self.__endereco}")
    
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_data_de_nascimento(self):
        return self.__data_de_nascimento

    def get_endereco(self):
        return self.__endereco

    @staticmethod
    def get_by_cpf(cpf):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('SELECT * FROM Aluno WHERE cpf = ?', (cpf,))
        result = cur.fetchall()

        cur.close()
        con.close()

        if result:
            result = list(result[0])
            return AlunoModel(result[0], result[1], result[2], result[3], result[4])
        else:
            return None

    @staticmethod
    def get_all_cpf():
        codigos = []

        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('SELECT cpf FROM Aluno')
        result = cur.fetchall()

        codigos = [row[0] for row in result]

        cur.close()
        con.close()

        return codigos

    @staticmethod
    def get_all():
        _all = []
        
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        
        cur.execute('SELECT * FROM Aluno')
        result = cur.fetchall()
        
        for i in result:
            row = list(i)
            _all.append(AlunoModel(row[0], row[1], row[2], row[3], row[4]))
        
        cur.close()
        con.close()
        
        return _all

    @staticmethod
    def delete_all():
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        
        cur.execute('DELETE FROM Aluno')
        con.commit()
        
        cur.close()
        con.close()

    @staticmethod
    def delete_by_cpf(cpf):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute('SELECT * FROM Aluno WHERE cpf = ?', (cpf,))
        if cur.fetchone() is None:
            cur.close()
            con.close()
            return ['err', 'Aluno(a) não localizado!']
        cur.execute('DELETE FROM Aluno WHERE cpf = ?', (cpf,))
        con.commit()
        cur.close()
        con.close()
        return ['msg', 'Deletado!']

    @staticmethod
    def save(cpf, nome, data_de_nascimento, email, endereco):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(
            """INSERT INTO Aluno VALUES (?, ?, ?, ?, ?)""",
            (cpf, nome, data_de_nascimento, email, endereco)
        )
        con.commit()
        cur.close()
        con.close()

    @staticmethod
    def update(cpf, nome, data_de_nascimento, email, endereco):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute("""
            UPDATE Aluno
            SET name = ?, aniversario = ?, email = ?, endereco = ?
            WHERE cpf = ?
        """, (nome, data_de_nascimento, email, endereco, cpf))

        con.commit()
        cur.close()
        con.close()
