import sqlite3
from config.db_config import DB_PATH

class DisciplinaModel:
    def __init__(self, codigo, nome, carga_horaria, professor):
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__professor = professor

    def __str__(self):
        return (f"Codigo: {self.__codigo}\nNome: {self.__nome}\nCarga Horaria: {self.__carga_horaria}\nProfessor Responsavel:{self.__professor}")
    
    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_carga_horaria(self):
        return self.__carga_horaria

    def get_professor(self):
        return self.__professor

    @staticmethod
    def get_by_codigo(codigo):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        
        cur.execute('SELECT * FROM Disciplina WHERE codigo = ?', (codigo,))
        result = cur.fetchall()
        result = list(result[0])
        
        cur.close()
        con.close()
        
        return DisciplinaModel(result[0], result[1], result[2], result[3])
    
    @staticmethod
    def get_all_codigos():
        codigos = []

        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('SELECT codigo FROM Disciplina')
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
        
        cur.execute('SELECT * FROM Disciplina')
        result = cur.fetchall()
        
        for i in result:
            row = list(i)
            _all.append(DisciplinaModel(row[0], row[1], row[2], row[3]))
        
        cur.close()
        con.close()
        
        return _all

    @staticmethod
    def delete_all():
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        
        cur.execute('DELETE FROM Disciplina')
        con.commit()
        
        cur.close()
        con.close()

    @staticmethod
    def delete_by_codigo(codigo):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute('SELECT * FROM Disciplina WHERE codigo = ?', (codigo,))
        if cur.fetchone() is None:
            cur.close()
            con.close()
            return ['err', 'Disciplina não localizada!']
        cur.execute('DELETE FROM Disciplina WHERE codigo = ?', (codigo,))
        con.commit()
        cur.close()
        con.close()
        return ['msg', 'Deletado!']

    @staticmethod
    def save(codigo, nome, carga_horaria, professor):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(f"""INSERT INTO Disciplina VALUES
                    ({codigo},'{nome}',{carga_horaria},'{professor}')""")
        con.commit()
        cur.close()
        con.close()

    @staticmethod
    def update(codigo, nome, carga_horaria, professor):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute("""
            UPDATE Disciplina
            SET name = ?, ch = ?, professor = ?
            WHERE codigo = ?
        """, (nome, carga_horaria, professor, codigo))

        con.commit()
        cur.close()
        con.close()
