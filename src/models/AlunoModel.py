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
        return str({'cpf':self.__cpf,
                    'nome':self.__nome,
                    'data_de_nascimento':self.__data_de_nascimento,
                    'email':self.__email,
                    'endereco': self.__endereco})

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
        cur.execute('DELETE FROM Aluno WHERE cpf = ?', (cpf,))
        con.commit()
        cur.close()
        con.close()

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
            SET nome = ?, data_de_nascimento = ?, email = ?, endereco = ?
            WHERE cpf = ?
        """, (nome, data_de_nascimento, email, endereco, cpf))

        con.commit()
        cur.close()
        con.close()
