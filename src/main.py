import sqlite3
from controllers.DisciplinaController import DisciplinaController
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
    dis_controller = DisciplinaController()
    print(dis_controller.set_carga_horaria(60))
    print(dis_controller.set_nome('POO'))
    print(dis_controller.set_codigo(6))
    print(dis_controller.set_professor("Fabio"))
    print(dis_controller.registrar())
    print(dis_controller.procurar_disciplina(60))
    l = dis_controller.listar_disciplinas()
    # l = DisciplinaModel.get_all()
    for i in l:
        print(i)
    


if __name__ == '__main__':
    main()