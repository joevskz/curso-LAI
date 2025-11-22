# artigo_conferencia.py (Herança)
from obra_cientifica import ObraCientifica


class ArtigoConferencia(ObraCientifica):
    def __init__(self, titulo, palavras_chave, resumo, autores,
                 evento, local_evento, data_evento, instituicao, titulo_anais, doi, ano, url):
        super().__init__(titulo, palavras_chave, resumo, autores)
        self.__evento = evento
        self.__local_evento = local_evento
        self.__titulo_anais = titulo_anais
        self.__doi = doi
        self.__ano = ano
        self.__instituicao = instituicao

    def get_tipo(self):
        return "Artigo de Conferência"

    def get_doi_isbn(self):
        return self.__doi

    def get_ano(self):
        return self.__ano

    def get_citacao_abnt(self):
        autores = self.get_autores_str()
        return (f"{autores}. {self.get_titulo()}. In: {self.__evento}, {self.__ano}, {self.__local_evento}. "
                f"**{self.__titulo_anais}**. {self.__instituicao}, {self.__ano}. DOI: {self.__doi}.")