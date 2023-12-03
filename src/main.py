import sqlite3
from views.DisciplinaMenu import DisciplinaMenu
from views.AlunoMenu import AlunoMenu
from views.Menu import Menu
from models.MatriculaModel import MatriculaModel
from config.db_config import TABLE_DISCIPLINA, TABLE_ALUNO, TABLE_MATRICULA
from config.db_config import DB_PATH

def call_configs():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(TABLE_DISCIPLINA)
    cur.execute(TABLE_ALUNO)
    cur.execute(TABLE_MATRICULA)
    cur.close()
    con.close()


def main_menu():
    while True:
        opcao = m.menu_de_opcoes(opt, "Menu Principal")
        if opcao == 1:
            m_disciplina.call_menu()
        elif opcao == 2:
            m_aluno.call_menu()
        elif opcao == 3:
            MatriculaModel.save(12345678915, 1)
        elif opcao == 4:
            exit()

if __name__ == '__main__':
    call_configs()
    m = Menu()
    m_disciplina = DisciplinaMenu()
    m_aluno = AlunoMenu()
    opt = [
        "Controle de Disciplinas",
        "Controle de Alunos(as)",
        "Controle de Matrículas",
        "Sair"
    ]
    main_menu()