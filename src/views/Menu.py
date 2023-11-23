import os

class Menu:
    def __init__(self):
        self.superior = "╔════════════════════════════════════════════════════╗"
        self.central  = "╠════════════════════════════════════════════════════╣"
        self.inferior = "╚════════════════════════════════════════════════════╝"

    def limpar_tela(self):
        """
        Limpa a tela do console de acordo com o sistema operacional.

        Returns:
            None
        """
        sistema_operacional = os.name
        if sistema_operacional == 'posix':  # Linux ou MacOS
            os.system('clear')
        elif sistema_operacional == 'nt':  # Windows
            os.system('cls')
        else:
            pass

    def menu_de_opcoes(self, opcoes, titulo=''):
        """
        Exibe um menu de opções e retorna a opção escolhida pelo usuário.

        Args:
            opcoes (list): Uma lista de strings representando as opções do menu.
            titulo (str, opcional): Um título opcional para o menu.

        Returns:
            int: O número da opção escolhida pelo usuário.

        Raises:
            None: Se a entrada do usuário não puder ser convertida para um número inteiro.
            None: Se a opção escolhida não estiver dentro do intervalo válido.
        """
        self.limpar_tela()
        print(self.superior)
        if(titulo != ''):
            print(f"║ {titulo.ljust(50)} ║")
            print(self.central)
        for opcao in opcoes:
            print(f"║ {opcoes.index(opcao) + 1}. {opcao.ljust(47)} ║")
        print(self.inferior)
        try:
            opc = int(input('● '))
            if opc not in range(1, len(opcoes) + 1):
                self.error("Opção Invalida!")
                return None
            else:
                return opc
        except:
            self.error("Opção Invalida!")
            return None


    def menu_input_check(self, texto, funcao_de_convercao):
        """
        Exibe um menu simples para entrada de dados e verifica se a conversão é bem-sucedida.

        Args:
            texto (str): O texto a ser exibido.
            funcao_de_convercao (callable): A função de conversão do dado. int, float, str...

        Returns:
            O dado de entrada convertido.

        Raises:
            Exception: return None
        """
        r = ''
        self.limpar_tela()
        print(self.superior)
        print(f"║ {texto.ljust(50)} ║")
        print(self.inferior)
        r = input('● ')
        try:
            r = funcao_de_convercao(r)
            return r
        except:
            self.error("Não foi possivel converter o Dado!")
            return None
        


    def error(self, err):
        """
        Exibe uma mensagem de erro formatada na tela.

        Args:
            err (str): A mensagem de erro a ser exibida.

        Returns:
            None
        """
        direita = int(25 - ((len(err)/2) + 6))
        esquerda = int(25 + (len(err)/2))
        self.limpar_tela()
        print(f"{self.superior}")
        print(f"║⚠{''.ljust(direita)}ERROR:{err.ljust(esquerda)}⚠║▒")
        print(f"{self.inferior}▒")
        print(" ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        input('')

    