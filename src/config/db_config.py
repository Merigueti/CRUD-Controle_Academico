DB_NAME = 'controle_academico.db'
DB_PATH = './' + DB_NAME

TABLE_DISCIPLINA = """
    CREATE TABLE IF NOT EXISTS Disciplina(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ch INTEGER NOT NULL,
    professor TEXT NOT NULL
    );
    """

TABLE_ALUNO = '''
    CREATE TABLE IF NOT EXISTS Aluno(
    cpf TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    aniversario DATE NOT NULL,
    email TEXT NOT NULL,
    endereco TEXT NOT NULL
    );
    '''

TABLE_MATRICULA = '''
    CREATE TABLE IF NOT EXISTS Matricula(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf_aluno TEXT NOT NULL,
    codigo_disciplina INTEGER NOT NULL,
    horario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cpf_aluno) REFERENCES Aluno(cpf) ON DELETE CASCADE,
    FOREIGN KEY (codigo_disciplina) REFERENCES Disciplina(codigo) ON DELETE CASCADE
    );
    '''

