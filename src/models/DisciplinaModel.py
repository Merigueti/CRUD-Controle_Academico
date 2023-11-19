import sqlite3
from config.db_config import DB_PATH

class DisciplinaModel:
    def __init__(self, codigo, nome, carga_horaria, professor):
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__professor = professor

    def __str__(self):
        return str({'codigo':self.__codigo,
                'nome':self.__nome,
                'carga_horaria':self.__carga_horaria,
                'professor':self.__professor})

    @staticmethod
    def get_by_code(code):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        
        cur.execute('SELECT * FROM Disciplina WHERE code = ?', (code,))
        result = cur.fetchall()
        result = list(result[0])
        
        cur.close()
        con.close()
        
        return DisciplinaModel(result[0], result[1], result[2], result[3])

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
    def delete_by_code(code):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute('DELETE FROM Disciplina WHERE code = ?', (code,))
        con.commit()
        cur.close()
        con.close()

    @staticmethod
    def save(codigo, nome, carga_horaria, professor):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(f"""INSERT INTO Disciplina VALUES
                    ({codigo},'{nome}',{carga_horaria},'{professor}')""")
        con.commit()
        cur.close()
        con.close()
