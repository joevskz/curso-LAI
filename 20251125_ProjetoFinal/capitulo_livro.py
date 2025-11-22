# capitulo_livro.py (Herança)
from obra_cientifica import ObraCientifica


class CapituloLivro(ObraCientifica):
    def __init__(self, titulo_capitulo, palavras_chave, resumo, autores,
                 titulo_livro, organizadores, editora, cidade, ano, isbn_doi, url):
        # Título da obra genérica recebe o título do capítulo aqui para listagens
        super().__init__(titulo_capitulo, palavras_chave, resumo, autores)
        self.__titulo_livro = titulo_livro
        self.__organizadores = organizadores
        self.__editora = editora
        self.__cidade = cidade
        self.__ano = ano
        self.__isbn_doi = isbn_doi
        self.__url = url

    def get_tipo(self):
        return "Capítulo de Livro"

    def get_doi_isbn(self):
        return self.__isbn_doi

    def get_ano(self):
        return self.__ano

    def get_citacao_abnt(self):
        autores = self.get_autores_str()
        return (f"{autores}. {self.get_titulo()}. In: {self.__organizadores} (Org.). "
                f"**{self.__titulo_livro}**. {self.__cidade}: {self.__editora}, {self.__ano}. "
                f"Identificador: {self.__isbn_doi}.")