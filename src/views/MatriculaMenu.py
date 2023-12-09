from views.Menu import Menu
from controllers.MatriculaController import MatriculaController

class MatriculaMenu(Menu):
    def __init__(self):
        super().__init__()
        self.mc = MatriculaController()
        self.opt = [
            'Matricular Aluno(a)',
            'Cancelar Matrícula',
            'Listar Matrículas',
            'Voltar Menu Principal'
        ]
    
    def call_menu(self):
        while True:
            opt = self.menu_de_opcoes(self.opt, 'Controle de Disciplinas')
            if opt == 1:
                self.cadatrar()
            if opt == 2:
                self.remover()
            elif opt == 3:
                self.listarMatriculas()
            elif opt == 4:
                break
        
        
    def cadatrar(self):
        while True:
            codigo = self.menu_input_check("Escreva o codigo da Disciplina ", int)
            if codigo is not None:
                ok = self.mc.set_codigo_disciplina(codigo)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break

        while True:
            cpf = self.menu_input_check("Escreva o cpf do aluno", str)
            if cpf is not None:
                ok = self.mc.set_cpf_aluno(cpf)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break
        
        ok = self.mc.registrar()
        if ok[0] == 'err':
            self.error(ok[1])

    def listarMatriculas(self):
        a = []
        lista = self.mc.listar_matriculas()
        for l in lista:
            a.append(str(l))
        self.listar(a)
        print(f"TOTAL DE MATRICULAS CADASTRADAS: {len(lista)}")
        input('')
        while True:
            opt = self.menu_de_opcoes(['Sim', 'Não'], 'Exportar para matriculas.csv?')
            if opt == 1:
                try:
                    self.mc.criar_csv(lista , "matriculas.csv")
                    self.menu_input_check("Arquivo criado!")
                    break
                except:
                    self.error("Erro ao criar arquivo!")
                    break
            elif opt == 2:
                break

    def remover(self):
        while True:
            codigo = self.menu_input_check("Escreva o codigo da Disciplina ", int)
            if codigo is not None:
                ok = self.mc.set_codigo_disciplina(codigo)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break

        while True:
            cpf = self.menu_input_check("Escreva o cpf do aluno", str)
            if cpf is not None:
                ok = self.mc.set_cpf_aluno(cpf)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break

        self.mc.deletar(cpf, codigo)
        