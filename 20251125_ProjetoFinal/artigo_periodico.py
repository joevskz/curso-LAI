# artigo_periodico.py (Herança)
from obra_cientifica import ObraCientifica

class ArtigoPeriodico(ObraCientifica):
    def __init__(self, titulo, palavras_chave, resumo, autores,
                 periodico, volume, numero, paginas, doi, ano, url, local):
        super().__init__(titulo, palavras_chave, resumo, autores)
        # Atributos privados específicos
        self.__periodico = periodico
        self.__volume = volume
        self.__numero = numero
        self.__paginas = paginas
        self.__doi = doi
        self.__ano = ano
        self.__local = local
        self.__url = url

    def get_tipo(self):
        return "Artigo de Periódico"

    def get_doi_isbn(self):
        return self.__doi

    def get_ano(self):
        return self.__ano

    # Polimorfismo
    def get_citacao_abnt(self):
        autores = self.get_autores_str()
        return (f"{autores}. {self.get_titulo()}. **{self.__periodico}**, {self.__local}, "
                f"v. {self.__volume}, n. {self.__numero}, p. {self.__paginas}, {self.__ano}. "
                f"DOI: {self.__doi}. Disponível em: {self.__url}.")