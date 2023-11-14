

def main():
    a = Aluno()
    m = Menu()
    if not a.set_cpf('169.666.627-98'):
        m.error("CPF INVALIDO!")
    print(a.get_cpf())
    a.set_data_de_nascimento(1997,6,17)
    print(a.get_idade())
    print(a.get_endereco_by_cep(29210440))


if __name__ == '__main__':
    main()