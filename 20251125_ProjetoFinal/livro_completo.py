# livro_completo.py
from obra_cientifica import ObraCientifica


class LivroCompleto(ObraCientifica):
    def __init__(self, titulo, palavras_chave, resumo, autores,
                 editora, cidade, ano, isbn_doi, url):
        super().__init__(titulo, palavras_chave, resumo, autores)
        self.__editora = editora
        self.__cidade = cidade
        self.__ano = ano
        self.__isbn_doi = isbn_doi
        self.__url = url

    def get_tipo(self):
        return "Livro Completo"

    def get_doi_isbn(self):
        return self.__isbn_doi

    def get_ano(self):
        return self.__ano

    def get_citacao_abnt(self):
        autores = self.get_autores_str()
        return (f"{autores}. **{self.get_titulo()}**. {self.__cidade}: {self.__editora}, {self.__ano}. "
                f"Identificador: {self.__isbn_doi}.")