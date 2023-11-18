DB_NAME = 'controle_academico.db'
DB_PATH = './' + DB_NAME

TABLE_DISCIPLINA = '''
    CREATE TABLE IF NOT EXISTS Disciplina(
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ch INTEGER NOT NULL,
    professor TEXT NOT NULL,
    );
    '''

