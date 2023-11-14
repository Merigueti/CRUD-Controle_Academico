import requests

class CepService:
    @staticmethod
    def get_endereco_por_cep(cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None