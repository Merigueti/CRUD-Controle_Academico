from views.Menu import Menu
from services.Cep_Service import CepService
from controllers.AlunoController import AlunoController

class AlunoMenu(Menu):
    def __init__(self):
        super().__init__()
        self.ac = AlunoController()
        self.opt = [
            'Cadastrar Aluno(a)',
            'Atualizar Aluno(a)',
            'Remover Aluno(a)',
            'Listar Alunos(as)',
            'Voltar Menu Principal'
        ]
    
    def call_menu(self):
        while True:
            opt = self.menu_de_opcoes(self.opt, 'Controle de Alunos(as)')
            if opt == 1:
                self.cadatrar()
            # if opt == 2:
            #     self.atualizar()
            # elif opt == 3:
            #     self.remover()
            # elif opt == 4:
            #     self.listarDis()
        
        
    def cadatrar(self):
        # while True:
        #     nome = self.menu_input_check("Escreva o nome do Aluno(a) ", str)
        #     if nome is not None:
        #         ok = self.ac.set_nome(nome)
        #         if ok[0] == 'err':
        #             self.error(ok[1])
        #         else:
        #             break

        # while True:
        #     dia = self.menu_input_check("Escreva o Dia que o aluno Nasceu.", int)
        #     if dia > 31 or dia < 1:
        #         self.error("DIA INVALIDO!")
        #     else:
        #         break
        
        # while True:
        #     mes = self.menu_input_check("Escreva o mês que o aluno Nasceu.", int)
        #     if mes > 12 or mes < 1:
        #         self.error("MÊS INVALIDO!")
        #     else:
        #         break

        # while True:
        #     ano = self.menu_input_check("Escreva o Ano que o aluno Nasceu.", int)
        #     if ano < 1900:
        #         self.error("ANO INVALIDO!")
        #     else:
        #         self.ac.set_data_de_nascimento(ano,mes,dia)
        #         self.menu_input_check(f"IDADE: {self.ac.get_idade()}", str)
        #         break
            
        # while True:
        #     email = self.menu_input_check("Escreva o email do Aluno", str)
        #     if email is not None:
        #         ok = self.ac.set_email(email)
        #         if ok[0] == 'err':
        #             self.error(ok[1])
        #         else:
        #             break
        
        while True:
            cep = self.menu_input_check("Escreva o CEP do Aluno", str)
            if cep is not None:
                endereco = CepService.get_endereco_por_cep(cep)
                print(endereco)
                input()
                break
        
        self.menu_input_check("Confirme o endereço, deixando em branco para confirmar\n ou digitando a informação correta para sobreescrever:", str)

        while True:
            logradouro = self.menu_input_check(f"Logradouro: {endereco['logradouro']}")
            if logradouro == None:
                logradouro = endereco.logradouro
            else:
                break
        
        
        # while True:
        #     codigo = self.menu_input_check("Escreva o codigo numerico referente a Disciplina", int)
        #     if codigo is not None:
        #         ok = self.dc.set_codigo(codigo)
        #         if ok[0] == 'err':
        #             self.error(ok[1])
        #         else:
        #             ok = self.dc.registrar()
        #             if ok[0] == 'err':
        #                 self.error(ok[1])
        #             else:
        #                 # O registro foi bem-sucedido, podemos sair do loop
        #                 break

    # def atualizar(self):
    #     try:
    #         codigo = self.menu_input_check('Escreva o codigo da Disciplina', int)
    #         ok = self.dc.load(codigo)
    #     except:
    #         self.error('Codigo Invalido!')
    #         return

    #     if ok[0] == 'msg':
    #         while True:
    #             nome = self.menu_input_check(f"Escreva o novo nome da Disciplina: [{self.dc.get_nome()}]", str)
    #             if nome is not None:
    #                 ok = self.dc.set_nome(nome)
    #                 if ok[0] == 'err':
    #                     self.error(ok[1])
    #                 else:
    #                     break
    #             else:
    #                 break

    #         while True:
    #             professor = self.menu_input_check(f"Escreva o nome do professor responsaval: [{self.dc.get_professor()}]", str)
    #             if professor is not None:
    #                 ok = self.dc.set_professor(professor)
    #                 if ok[0] == 'err':
    #                     self.error(ok[1])
    #                 else:
    #                     break
    #             else:
    #                 break

    #         while True:
    #             ch = self.menu_input_check(f"Escreva a carga horaria em Horas: [{self.dc.get_carga_horaria()}]", str)
    #             if ch == '':
    #                 break
    #             else:
    #                 try:
    #                     int(ch)
    #                 except:
    #                     self.error("Não foi possivel converter o Dado!")
    #             if ch is not None:
    #                 ok = self.dc.set_carga_horaria(ch)
    #                 if ok[0] == 'err':
    #                     self.error(ok[1])
    #                 else:
    #                     break
    #             else:
    #                 break
            
    #         ok = self.dc.atualizar()
    #         if ok[0] == 'err':
    #             self.error(ok[1])
    #         else:
    #             self.menu_input_check(f"Modificaçoes salvas!", str)

    # def listarDis(self):
    #     a = []
    #     lista = self.dc.listar_disciplinas()
    #     for l in lista:
    #         a.append(str(l))
    #     self.listar(a)
    #     input('')

    # def remover(self):
    #     codigo = self.menu_input_check('Escreva o codigo da Disciplina', int)
    #     ok = self.dc.deletar(codigo)
    #     if ok[0] == 'err':
    #         self.error(ok[1])
    #     else:
    #         self.menu_input_check(ok[1], str)
        