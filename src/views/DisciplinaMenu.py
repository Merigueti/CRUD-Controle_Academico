from views.Menu import Menu
from controllers.DisciplinaController import DisciplinaController

class DisciplinaMenu(Menu):
    def __init__(self):
        super().__init__()
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
            opt = self.menu_de_opcoes(self.opt, 'Controle de Disciplinas')
            if opt == 1:
                self.cadatrar()
            if opt == 2:
                self.atualizar()
            elif opt == 3:
                self.remover()
            elif opt == 4:
                self.listarDis()
            elif opt == 5:
                break
        
        
    def cadatrar(self):
        while True:
            nome = self.menu_input_check("Escreva o nome da Disciplina ", str)
            if nome is not None:
                ok = self.dc.set_nome(nome)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break

        while True:
            professor = self.menu_input_check("Escreva o nome do professor responsaval", str)
            if professor is not None:
                ok = self.dc.set_professor(professor)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break

        while True:
            ch = self.menu_input_check("Escreva a carga horaria em Horas", int)
            if ch is not None:
                ok = self.dc.set_carga_horaria(ch)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break
        
        while True:
            codigo = self.menu_input_check("Escreva o codigo numerico referente a Disciplina", int)
            if codigo is not None:
                ok = self.dc.set_codigo(codigo)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    ok = self.dc.registrar()
                    if ok[0] == 'err':
                        self.error(ok[1])
                    else:
                        # O registro foi bem-sucedido, podemos sair do loop
                        break

    def atualizar(self):
        try:
            codigo = self.menu_input_check('Escreva o codigo da Disciplina', int)
            ok = self.dc.load(codigo)
        except:
            self.error('Codigo Invalido!')
            return

        if ok[0] == 'msg':
            while True:
                nome = self.menu_input_check(f"Escreva o novo nome da Disciplina: [{self.dc.get_nome()}]", str)
                if nome is not None:
                    ok = self.dc.set_nome(nome)
                    if ok[0] == 'err':
                        self.error(ok[1])
                    else:
                        break
                else:
                    break

            while True:
                professor = self.menu_input_check(f"Escreva o nome do professor responsaval: [{self.dc.get_professor()}]", str)
                if professor is not None:
                    ok = self.dc.set_professor(professor)
                    if ok[0] == 'err':
                        self.error(ok[1])
                    else:
                        break
                else:
                    break

            while True:
                ch = self.menu_input_check(f"Escreva a carga horaria em Horas: [{self.dc.get_carga_horaria()}]", str)
                if ch == '':
                    break
                else:
                    try:
                        int(ch)
                    except:
                        self.error("Não foi possivel converter o Dado!")
                if ch is not None:
                    ok = self.dc.set_carga_horaria(ch)
                    if ok[0] == 'err':
                        self.error(ok[1])
                    else:
                        break
                else:
                    break
            
            ok = self.dc.atualizar()
            if ok[0] == 'err':
                self.error(ok[1])
            else:
                self.menu_input_check(f"Modificaçoes salvas!", str)

    def listarDis(self):
        a = []
        lista = self.dc.listar_disciplinas()
        for l in lista:
            a.append(str(l))
        self.listar(a)
        print(f"TOTAL DE DISCIPLINAS CADASTRADAS: {len(lista)}")
        input('')
        while True:
            opt = self.menu_de_opcoes(['Sim', 'Não'], 'Exporta para disciplinas.csv?')
            if opt == 1:
                try:
                    self.dc.criar_csv(lista , "disciplinas.csv")
                    self.menu_input_check("Arquivo criado!")
                    break
                except:
                    self.error("Erro ao criar arquivo!")
                    break
            elif opt == 2:
                break

    def remover(self):
        codigo = self.menu_input_check('Escreva o codigo da Disciplina', int)
        ok = self.dc.deletar(codigo)
        if ok[0] == 'err':
            self.error(ok[1])
        else:
            self.menu_input_check(ok[1], str)
        