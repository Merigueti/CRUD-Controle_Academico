from datetime import datetime
import requests

class Aluno:
    def __init__(self):
        self.__cpf = ''
        self.__nome = ''
        self.__data_de_nascimento = []
        self.__email = ''
        self.__endereco = {'cep': '', 
                           'logradouro': '', 
                           'bairro': '', 
                           'localidade': '', 
                           'uf': ''}

    # Getter methods
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        hoje = datetime.today() 
        idade = hoje.year - self.__data_de_nascimento.year 
        - ((hoje.month, hoje.day) 
           < (self.__data_de_nascimento.month, 
              self.__data_de_nascimento.day)) 
    
        return idade

    def get_email(self):
        return self.__email

    def get_endereco(self):
        return self.__endereco
    
    def get_endereco_by_cep(self, cep=''):
        pass

    # Setter methods
    def set_cpf(self, cpf):
        cpf_tratado = ''.join(caractere for caractere in cpf if caractere.isdigit())
        if len(cpf_tratado) == 11:
            self.__cpf = cpf_tratado
            return True
        else:
            return False

    def set_nome(self, nome):
        self.__nome = nome

    def set_data_de_nascimento(self, ano, mes, dia):
        self.__data_de_nascimento = datetime(ano,mes,dia)

    def set_email(self, email):
        self.__email = email

    def set_endereco(self, cep, logradouro, bairro, localidade, uf):
        self.__endereco['cep'] = cep
        self.__endereco['logradouro'] = logradouro
        self.__endereco['bairro'] = bairro
        self.__endereco['localidade'] = localidade
        self.__endereco['uf'] = uf

    