# pesquisador.py

class Pesquisador:
    """
    Classe que representa um membro do grupo de pesquisa.
    Atributos privados para garantir encapsulamento.
    """
    def __init__(self, nome, cpf, email, celular, lattes, orcid, programa, instituicao, tipo, vinculo):
        # Atributos Privados (Encapsulamento)
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__celular = celular
        self.__lattes = lattes
        self.__orcid = orcid
        self.__programa = programa # Ex: PGCIN
        self.__instituicao = instituicao # Ex: UFSC, UFMG
        self.__tipo = tipo      # Ex: Doutorando, Mestrando, Docente
        self.__vinculo = vinculo # Ex: bolsista, voluntário, contratado, magistério

    # Getters
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_tipo(self):
        return self.__tipo

    def __str__(self):
        """Retorna string formatada para relatórios de perfil."""
        return (f"Nome: {self.__nome} | Tipo: {self.__tipo} | Inst.: {self.__instituicao}\n"
                f"   Email: {self.__email} | Lattes: {self.__lattes}")