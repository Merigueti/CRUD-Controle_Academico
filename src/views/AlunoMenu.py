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
            #elif if opt == 2:
            #     self.atualizar()
            elif opt == 3:
                self.remover()
            elif opt == 4:
                self.listarAlunos()
            elif opt == 5:
                break
        
    def cadatrar(self):
        while True:
            nome = self.menu_input_check("Escreva o nome do Aluno(a) ", str)
            if nome is not None:
                ok = self.ac.set_nome(nome)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break

        while True:
            dia = self.menu_input_check("Escreva o Dia que o aluno Nasceu.", int)
            if dia is not None:
                if dia > 31 or dia < 1:
                    self.error("DIA INVALIDO!")
                else:
                    break
        
        while True:
            mes = self.menu_input_check("Escreva o mês que o aluno Nasceu.", int)
            if mes is not None:
                if mes > 12 or mes < 1:
                    self.error("MÊS INVALIDO!")
                else:
                    break

        while True:
            ano = self.menu_input_check("Escreva o Ano que o aluno Nasceu.", int)
            if ano is not None:
                if ano < 1900:
                    self.error("ANO INVALIDO!")
                else:
                    self.ac.set_data_de_nascimento(ano,mes,dia)
                    self.menu_input_check(f"IDADE: {self.ac.get_idade()}", str)
                    break
            
        while True:
            email = self.menu_input_check("Escreva o email do Aluno", str)
            if email is not None:
                ok = self.ac.set_email(email)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    break
        
        while True:
            cep = self.menu_input_check("Escreva o CEP do Aluno", str)
            if cep is not None:
                endereco = CepService.get_endereco_por_cep(cep)
                if endereco == None:
                    endereco = {}
                    endereco['cep'] = cep
                    endereco['logradouro'] = 'Não encontrado'
                    endereco['bairro'] = 'Não encontrado'
                    endereco['localidade'] = 'Não Encontrado'
                    endereco['uf'] = 'Não Encontrado'
                break
            else:
                break
        
        self.menu_input_check("Para confirmar, deixe o endereço em branco \nou insira a informação correta para substituir")

        while True:
            logradouro = self.menu_input_check(f"Logradouro: {endereco['logradouro']}", str)
            if logradouro == '':
                logradouro = endereco['logradouro']
                break
            else:
                break

        while True:
            bairro = self.menu_input_check(f"Bairro: {endereco['bairro']}", str)
            if bairro == '':
                bairro = endereco['bairro']
                print(bairro)
                break
            else:
                break
        
        while True:
            localidade = self.menu_input_check(f"Cidade: {endereco['localidade']}", str)
            if localidade == '':
                localidade = endereco['localidade']
                break
            else:
                break
        
        while True:
            uf = self.menu_input_check(f"Estado: {endereco['uf']}", str)
            if uf == '':
                uf = endereco['uf']
                break
            else:
                break
        
        self.ac.set_endereco(cep,logradouro,bairro,localidade,uf)
        print(self.ac.get_endereco())
        input()
        
        while True:
            cpf = self.menu_input_check("Escreva o CPF do Aluno", str)
            if cpf is not None:
                ok = self.ac.set_cpf(cpf)
                if ok[0] == 'err':
                    self.error(ok[1])
                else:
                    ok = self.ac.registrar()
                    if ok[0] == 'err':
                        self.error(ok[1])
                    else:
                        break

    def atualizar(self):
        try:
            codigo = self.menu_input_check('Escreva o codigo da Disciplina', int)
            ok = self.dc.load(codigo)
        except:
            self.error('Codigo Invalido!')
            return

        

    def listarAlunos(self):
        a = []
        lista = self.ac.listar_alunos()
        for l in lista:
            a.append(str(l))
        self.listar(a)
        input('')

    def remover(self):
        self.ac.set_cpf("00000000000")
        cpf = self.menu_input_check('Escreva o CPF do Aluno que deseja remover', str)
        ok = self.ac.set_cpf(cpf)
        if ok[0] == 'err':
            ok = self.ac.deletar()
            if ok[0] == 'err':
                self.error(ok[1])
            else:
                self.menu_input_check(ok[1], str)
        else:
            self.error("CPF NÃO ENCONTRADO!")
        
        