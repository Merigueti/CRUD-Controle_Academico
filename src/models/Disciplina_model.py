class Disciplina_md:
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
        pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def delete_all():
        pass

    @staticmethod
    def delete_by_code(code):
        pass