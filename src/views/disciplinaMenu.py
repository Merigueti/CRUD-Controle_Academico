from Menu import Menu
from controllers.DisciplinaController import DisciplinaController

class disciplinaMenu(Menu):
    def __init__(self):
        self.dc = DisciplinaController()
        self.opt = [
            'Cadastrar Nova Disciplina',
            'Atualizar Disciplina',
            'Remover Disciplina',
            'Listar Disciplinas',
            'Voltar Menu Principal'
        ]
    
    def call_menu(self):
        opt = None
        while opt == None:
            opt = self.menu_de_opcoes(self.opt, 'Controle de Disciplinas')
        if opt == 1:
            self.cadatrar()
        
    def cadatrar(self):
        while True:
            nome = self.menu_input_check("Escreva o nome da Disciplina ", str)
            ok = self.dc.set_nome(nome)
            if ok == 'err':
                self.error(ok[1])
            else:
                break

        while True:
            professor = self.menu_input_check("Escreva o nome do professor responsaval", str)
            ok = self.dc.set_professor(professor)
            if ok == 'err':
                self.error(ok[1])
            else:
                break

        while True:
            ch = self.menu_input_check("Escreva a carga horaria em Horas", int)
            ok = self.dc.set_carga_horaria(ch)
            if ok == 'err':
                self.error(ok[1])
            else:
                break
        
        while True:
            codigo = self.menu_input_check("Escreva o codigo numerico referente a Disciplina", int)
            ok = self.dc.set_codigo(codigo)
            if ok == 'err':
                self.error(ok[1])
            else:
                break
            
        
        


        