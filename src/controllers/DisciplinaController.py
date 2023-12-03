from models.DisciplinaModel import DisciplinaModel

class DisciplinaController:
    def __init__(self):
        self.__codigo = ''
        self.__nome = ''
        self.__carga_horaria = ''
        self.__professor = ''

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_carga_horaria(self):
        return self.__carga_horaria

    def get_professor(self):
        return self.__professor

    def procurar_disciplina(self, codigo):
        disiciplina = DisciplinaModel.get_by_codigo(codigo)
        return disiciplina
    
    def set_codigo(self, codigo):
        lista_de_codigos = DisciplinaModel.get_all_codigos()

        if codigo in lista_de_codigos:
            return ['err', 'Código em uso!']

        self.__codigo = codigo
        return ['msg', 'Código salvo com sucesso!']

    def set_nome(self, nome):
        if nome != '':
            self.__nome = nome
        return ['msg', 'Nome salvo com sucesso!']

    def set_carga_horaria(self, carga_horaria):
        if carga_horaria != '':
            self.__carga_horaria = carga_horaria
        return ['msg', 'Carga Horaria salva com sucesso!']

    def set_professor(self, professor):
        if professor != '':
            self.__professor = professor
        return ['msg', 'Professor responsavel salvo com sucesso!']

    def listar_disciplinas(self):
        l = DisciplinaModel.get_all()
        return l
    
    def load(self, codigo):
        dis = self.procurar_disciplina(codigo)
        self.__codigo = dis.get_codigo()
        self.__nome = dis.get_nome()
        self.__carga_horaria = dis.get_carga_horaria()
        self.__professor = dis.get_professor()
        if dis is not None:
            return ['msg', 'Disciplina carregada com sucesso!']
        else:
            return ['err', 'Erro ao carregar parametros!']

    def deletar(self, codigo):
        ok = DisciplinaModel.delete_by_codigo(codigo)
        return ok

    def atualizar(self):
        try:
            DisciplinaModel.update(self.__codigo, self.__nome, self.__carga_horaria, self.__professor)
            return ['msg', 'Disciplina salva com sucesso!']
        except:
            return ['err', 'Erro ao salva Disciplina!']

    def registrar(self):
        try:
            DisciplinaModel.save(self.__codigo, self.__nome, self.__carga_horaria, self.__professor)
            return ['msg', 'Disciplina salva com sucesso!']
        except:
            return ['err', 'Erro ao salva Disciplina!']
