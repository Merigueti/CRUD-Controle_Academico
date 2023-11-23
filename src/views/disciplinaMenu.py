from views.Menu import Menu
from controllers.DisciplinaController import DisciplinaController

class disciplinaMenu:
    def __init__(self):
        self.m = Menu()
        self.dc = DisciplinaController()
        self.opt = [
            'Cadastrar Nova Disciplina',
            'Atualizar Disciplina',
            'Remover Disciplina',
            'Listar Disciplinas',
            'Voltar Menu Principal'
        ]
    
    def call_menu(self):
        while True:
            opt = self.m.menu_de_opcoes(self.opt, 'Controle de Disciplinas')
            if opt == 1:
                self.cadatrar()
            elif opt == 4:
                self.listar()
        
        
    def cadatrar(self):
        while True:
            nome = self.m.menu_input_check("Escreva o nome da Disciplina ", str)
            if nome is not None:
                ok = self.dc.set_nome(nome)
                if ok[0] == 'err':
                    self.m.error(ok[1])
                else:
                    break

        while True:
            professor = self.m.menu_input_check("Escreva o nome do professor responsaval", str)
            if professor is not None:
                ok = self.dc.set_professor(professor)
                if ok[0] == 'err':
                    self.m.error(ok[1])
                else:
                    break

        while True:
            ch = self.m.menu_input_check("Escreva a carga horaria em Horas", int)
            if ch is not None:
                ok = self.dc.set_carga_horaria(ch)
                if ok[0] == 'err':
                    self.m.error(ok[1])
                else:
                    break
        
        while True:
            codigo = self.m.menu_input_check("Escreva o codigo numerico referente a Disciplina", int)
            if codigo is not None:
                ok = self.dc.set_codigo(codigo)
                if ok[0] == 'err':
                    self.m.error(ok[1])
                else:
                    ok = self.dc.registrar()
                    if ok[0] == 'err':
                        self.m.error(ok[1])
                    else:
                        # O registro foi bem-sucedido, podemos sair do loop
                        break

    def listar(self):
        a = []
        lista = self.dc.listar_disciplinas()
        for l in lista:
            a.append(str(l))
        self.m.listar(a)
        input('')


        