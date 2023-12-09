from models.MatriculaModel import MatriculaModel
from models.AlunoModel import AlunoModel
from models.DisciplinaModel import DisciplinaModel
import csv
class MatriculaController:
    def __init__(self):
        self.__id = ''
        self.__cpf_aluno = ''
        self.__codigo_disciplina = ''
        self.__horario = ''

    def get_id(self):
        return self.__id

    def get_cpf_aluno(self):
        return self.__cpf_aluno

    def get_codigo_disciplina(self):
        return self.__codigo_disciplina

    def get_horario(self):
        return self.__horario
    
    def criar_csv(self, lista_matriculas, nome_arquivo):
        with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
            _csv = csv.writer(arquivo_csv, delimiter=';')
            _csv.writerow(["Horário", "CPF do Aluno", "Código Disciplina"])
            for mt in lista_matriculas:
                _csv.writerow(f"{mt.get_horario()};{mt.get_cpf_aluno()};{mt.get_codigo_disciplina()};".split(';'))
    
    def set_cpf_aluno(self, cpf):
        cpf_tratado = ''.join(caractere for caractere in cpf if caractere.isdigit())
        lista_de_cpfs = AlunoModel.get_all_cpf()
        if cpf_tratado in lista_de_cpfs:
            self.__cpf_aluno = cpf_tratado
            return ['msg', 'CPF Encontrado!']
        return ['err', 'CPF não cadastrado!']
        
    def set_codigo_disciplina(self, codigo):
        lista_de_codigos = DisciplinaModel.get_all_codigos()
        if codigo in lista_de_codigos:
            self.__codigo_disciplina = codigo
            return ['msg', 'Codigo Encontrado']
        return ['err', 'Código não cadastrado!']

    def listar_matriculas(self):
        matriculas = MatriculaModel.get_all()
        return matriculas

    def deletar(self, cpf, codigo):
        ok = MatriculaModel.delete_by_cpf_and_codigo(cpf, codigo)
        return ok

    def registrar(self):
        try:
            MatriculaModel.save(self.__cpf_aluno, self.__codigo_disciplina)
            return ['msg', 'Matrícula registrada com sucesso!']
        except:
            return ['err', 'Erro ao registrar Matrícula!']
