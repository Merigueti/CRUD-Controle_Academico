class Disciplina:
    def __init__(self):
        self.__codigo = ''
        self.__nome = ''
        self.__carga_horaria = ''
        self.__professor = ''

    # Métodos get
    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_carga_horaria(self):
        return self.__carga_horaria

    def get_professor_responsavel(self):
        return self.__professor

    # Métodos set
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_nome(self, nome):
        self.__nome = nome

    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    def set_professor(self, professor):
        self.__professor = professor