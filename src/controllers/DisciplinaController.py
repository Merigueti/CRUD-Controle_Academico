from models.DisciplinaModel import DisciplinaModel

class DisciplinaController:
    def __init__(self):
        self.__codigo = ''
        self.__nome = ''
        self.__carga_horaria = ''
        self.__professor = ''

    def procurar_disciplina(self, codigo):
        disiciplina = DisciplinaModel.get_by_code(codigo)
        return disiciplina
    
    # Métodos set
    def set_codigo(self, codigo):
        if(codigo != ''):
            DisciplinaModel.get_all()
            self.__codigo = codigo
            return True
        else:
            pass

    def set_nome(self, nome):
        if nome != '':
            self.__nome = nome

    def set_carga_horaria(self, carga_horaria):
        if carga_horaria != '':
            self.__carga_horaria = carga_horaria

    def set_professor(self, professor):
        if professor != '':
            self.__professor = professor

    def listar():
        lista = DisciplinaModel.get_all()
        return lista

    def save(self, codigo, nome, carga_horaria, professor):
        try:
            self.set_codigo(codigo)
            self.set_nome(nome)
            self.set_carga_horaria(carga_horaria)
            self.set_professor(professor)
            DisciplinaModel.save(self.__codigo, self.__nome, self.__carga_horaria, self.__professor)
            return 'Disciplina salva com sucesso'
        except:
            return 'err'
