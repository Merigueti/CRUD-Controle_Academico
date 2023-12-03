import sqlite3
from config.db_config import DB_PATH

class MatriculaModel:
    def __init__(self, id, cpf_aluno, codigo_disciplina, horario):
        self.__id = id
        self.__cpf_aluno = cpf_aluno
        self.__codigo_disciplina = codigo_disciplina
        self.__horario = horario

    def __str__(self):
        return (f"ID: {self.__id}\nCPF Aluno: {self.__cpf_aluno}\nCódigo Disciplina: {self.__codigo_disciplina}\nHorário: {self.__horario}")

    def get_id(self):
        return self.__id

    def get_cpf_aluno(self):
        return self.__cpf_aluno

    def get_codigo_disciplina(self):
        return self.__codigo_disciplina

    def get_horario(self):
        return self.__horario

    @staticmethod
    def get_by_id(id):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('SELECT * FROM Matricula WHERE id = ?', (id,))
        result = cur.fetchall()
        if not result:
            return None

        result = list(result[0])

        cur.close()
        con.close()

        return MatriculaModel(result[0], result[1], result[2], result[3])

    @staticmethod
    def get_all_ids():
        ids = []

        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('SELECT id FROM Matricula')
        result = cur.fetchall()

        ids = [row[0] for row in result]

        cur.close()
        con.close()

        return ids

    @staticmethod
    def get_all():
        _all = []

        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('SELECT * FROM Matricula')
        result = cur.fetchall()

        for i in result:
            row = list(i)
            _all.append(MatriculaModel(row[0], row[1], row[2], row[3]))

        cur.close()
        con.close()

        return _all

    @staticmethod
    def delete_all():
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('DELETE FROM Matricula')
        con.commit()

        cur.close()
        con.close()

    @staticmethod
    def delete_by_id(id):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute('SELECT * FROM Matricula WHERE id = ?', (id,))
        if cur.fetchone() is None:
            cur.close()
            con.close()
            return ['err', 'Matrícula não localizada!']

        cur.execute('DELETE FROM Matricula WHERE id = ?', (id,))
        con.commit()
        cur.close()
        con.close()
        return ['msg', 'Matrícula Deletada!']

    @staticmethod
    def save(cpf_aluno, codigo_disciplina):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute('SELECT * FROM Matricula WHERE cpf_aluno = ? AND codigo_disciplina = ?', (cpf_aluno, codigo_disciplina))
        existing_matricula = cur.fetchone()

        if existing_matricula:
            con.close()
            return ['err', 'Aluno já matriculado nesta disciplina!']

        # Inserir a nova matrícula
        cur.execute('INSERT INTO Matricula (cpf_aluno, codigo_disciplina) VALUES (?, ?)', (cpf_aluno, codigo_disciplina))
        con.commit()
        cur.close()
        con.close()

        return ['msg', 'Matrícula realizada com sucesso!']
