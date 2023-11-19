DB_NAME = 'controle_academico.db'
DB_PATH = './' + DB_NAME

TABLE_DISCIPLINA = """
    CREATE TABLE IF NOT EXISTS Disciplina(
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ch INTEGER NOT NULL,
    professor TEXT NOT NULL
    );
    """

TABLE_ALUNO = '''
    CREATE TABLE IF NOT EXISTS Aluno(
    cpf TEXT NOT NULL,
    name TEXT NOT NULL,
    aniversario DATE NOT NULL,
    email TEXT NOT NULL,
    endereco TEXT NOT NULL
    );
    '''

