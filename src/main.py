import sqlite3
from views.disciplinaMenu import disciplinaMenu
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
    m_disciplina = disciplinaMenu()
    m_disciplina.call_menu()
    
    


if __name__ == '__main__':
    main()