import sqlite3
from models.DisciplinaModel import DisciplinaModel
from config.db_config import TABLE_DISCIPLINA, TABLE_ALUNO
from config.db_config import DB_PATH

def call_configs():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(TABLE_DISCIPLINA)
    cur.execute(TABLE_ALUNO)
    cur.close()
    con.close()

def main():
    call_configs()

    DisciplinaModel.save(0,"poo",60,"Jorge")
    DisciplinaModel.save(1,"batata",30,"Hiago")
    lista = DisciplinaModel.get_all()
    for l in lista:
        print(l)

    DisciplinaModel.delete_by_code(0)

    lista = DisciplinaModel.get_all()
    for l in lista:
        print(l)

if __name__ == '__main__':
    main()