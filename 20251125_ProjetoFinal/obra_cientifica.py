# obra_cientifica.py
from abc import ABC, abstractmethod
from constantes import ETAPAS_PRODUCAO, ETAPAS_PUBLICACAO, ETAPAS_DIFUSAO, CANAIS_DIFUSAO


class ObraCientifica(ABC):
    """
    Superclasse Abstrata que define o esqueleto de qualquer obra científica.
    Gerencia o estado (Produção -> Publicação -> Difusão).
    """

    def __init__(self, titulo, palavras_chave, resumo, autores):
        # Atributos privados mínimos exigidos (Encapsulamento)
        self.__titulo = titulo
        self.__palavras_chave = palavras_chave
        self.__resumo = resumo
        self.__autores = autores  # Lista de objetos Pesquisador

        # Controle de Estado
        self.__processo_atual = "Produção"  # Produção, Publicação, Difusão
        self.__indice_etapa = 0  # Index 0-based para listas em constantes.py

        # Dicionário para controlar difusão por canal independentemente
        # Chave: Canal, Valor: Indice da etapa de difusão
        self.__status_difusao = {canal: -1 for canal in CANAIS_DIFUSAO}

        # Getters necessários

    def get_titulo(self):
        return self.__titulo

    def get_processo_atual(self):
        return self.__processo_atual

    def get_indice_etapa(self):
        return self.__indice_etapa

    def get_status_difusao(self):
        return self.__status_difusao

    def get_autores_str(self):
        """Formata autores para ABNT (SOBRENOME, Nome; ...)"""
        nomes_abnt = []
        for autor in self.__autores:
            partes = autor.get_nome().split()
            sobrenome = partes[-1].upper()
            nome = " ".join(partes[:-1])
            nomes_abnt.append(f"{sobrenome}, {nome}")
        return "; ".join(nomes_abnt)

    # Métodos de lógica de negócio
    def set_etapa_manual(self, processo, indice_etapa):
        """Metodo utilitário para forçar um estado (usado no seeding de dados)."""
        self.__processo_atual = processo
        self.__indice_etapa = indice_etapa
        # Se forçar difusão, assume que já publicou
        if processo == "Difusão":
            # Inicializa difusão no estágio 0 para todos
            self.__status_difusao = {canal: 0 for canal in CANAIS_DIFUSAO}

    def set_status_difusao_canal(self, canal, indice):
        """Define o progresso da difusão para um canal específico."""
        if canal in self.__status_difusao:
            self.__status_difusao[canal] = indice

    def get_nome_etapa_atual(self):
        if self.__processo_atual == "Produção":
            return ETAPAS_PRODUCAO[self.__indice_etapa]
        elif self.__processo_atual == "Publicação":
            return ETAPAS_PUBLICACAO[self.__indice_etapa]
        else:
            return "Em Difusão (Múltiplos Canais)"

    def get_progresso_formatado(self):
        """Retorna string (X/Y concluídas)."""
        if self.__processo_atual == "Produção":
            total = len(ETAPAS_PRODUCAO)
            return f"({self.__indice_etapa + 1}/{total} concluídas)"
        elif self.__processo_atual == "Publicação":
            total = len(ETAPAS_PUBLICACAO)
            return f"({self.__indice_etapa + 1}/{total} concluídas)"
        return "(Concluído)"

    @abstractmethod
    def get_citacao_abnt(self):
        """Metodo polimórfico que deve ser implementado pelas subclasses."""
        pass

    @abstractmethod
    def get_tipo(self):
        pass

    @abstractmethod
    def get_doi_isbn(self):
        pass