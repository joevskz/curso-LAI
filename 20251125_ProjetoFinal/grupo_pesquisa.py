# grupo_pesquisa.py (Classe controladora para gerar os relatórios.)
from constantes import ETAPAS_DIFUSAO

class GrupoPesquisa:
    def __init__(self):
        self.__membros = []
        self.__obras = []

    def adicionar_membro(self, membro):
        self.__membros.append(membro)

    def adicionar_obra(self, obra):
        self.__obras.append(obra)

    # ---------------------------------------------------------
    # Relatório 3: Status de Disseminação Científica
    # ---------------------------------------------------------
    def relatorio_disseminacao(self):
        print("\n=== Relatório 3: Status de Disseminação Científica ===")

        # Filtrar e Ordenar (Decrescente por índice da etapa)
        prod = [o for o in self.__obras if o.get_processo_atual() == "Produção"]
        prod.sort(key=lambda x: x.get_indice_etapa(), reverse=True)

        pub = [o for o in self.__obras if o.get_processo_atual() == "Publicação"]
        pub.sort(key=lambda x: x.get_indice_etapa(), reverse=True)

        print("\n--- Processo: Produção ---")
        for i, obra in enumerate(prod, 1):
            print(f"{i}. [{obra.get_tipo()}] {obra.get_titulo()}")
            print(f"   Status: {obra.get_nome_etapa_atual()} {obra.get_progresso_formatado()}")

        print("\n--- Processo: Publicação ---")
        for i, obra in enumerate(pub, 1):
            print(f"{i}. [{obra.get_tipo()}] {obra.get_titulo()}")
            print(f"   Status: {obra.get_nome_etapa_atual()} {obra.get_progresso_formatado()}")

    # ---------------------------------------------------------
    # Relatório 4: Status da Difusão Científica
    # ---------------------------------------------------------
    def relatorio_difusao(self):
        print("\n=== Relatório 4: Status da Difusão Científica ===")
        # Obras em Difusão ou Publicação finalizada contam aqui se estiverem ativas
        obras_difusao = [o for o in self.__obras if o.get_processo_atual() == "Difusão"]

        for i, obra in enumerate(obras_difusao, 1):
            print(f"{i}. [{obra.get_tipo()}] {obra.get_titulo()} - DOI/ISBN: {obra.get_doi_isbn()}")
            status_canais = obra.get_status_difusao()
            for canal, indice in status_canais.items():
                if indice >= 0:  # Se o canal foi ativado
                    nome_etapa = ETAPAS_DIFUSAO[indice] if indice < len(ETAPAS_DIFUSAO) else "Concluído"
                    progresso = f"({indice + 1}/{len(ETAPAS_DIFUSAO)} concluídas)"
                    print(f"   - {canal}: {nome_etapa} {progresso}")
                else:
                    print(f"   - {canal}: Não iniciado")

    # ---------------------------------------------------------
    # Relatório 2: Portfólio (ABNT)
    # ---------------------------------------------------------
    def relatorio_portfolio(self):
        print("\n=== Relatório 2: Portfólio do Grupo de Pesquisa ===")
        # Filtra obras Publicação (etapa final) ou Difusão
        candidatas = [o for o in self.__obras if o.get_processo_atual() == "Difusão" or
                      (o.get_processo_atual() == "Publicação" and o.get_nome_etapa_atual() == "Publicação final")]

        # Segregar por tipo
        tipos = ["Artigo de Periódico", "Artigo de Conferência", "Capítulo de Livro", "Livro Completo"]

        for tipo in tipos:
            lista_tipo = [o for o in candidatas if o.get_tipo() == tipo]
            # Ordenar decrescente por ano (assumindo que temos acesso ao ano)
            # Para simplificar, usa-se o atributo privado via metodo específico se existir
            # ou assume-se ordenação na inserção. Vamos tentar ordenar.
            lista_tipo.sort(key=lambda x: getattr(x, 'get_ano', lambda: 0)(), reverse=True)

            if lista_tipo:
                print(f"\n--- {tipo}s ---")
                for obra in lista_tipo:
                    print(f"- {obra.get_citacao_abnt()}")

    # ---------------------------------------------------------
    # Relatório 5: Produtividade
    # ---------------------------------------------------------
    def relatorio_produtividade(self):
        print("\n=== Relatório 5: Produtividade do Grupo ===")
        # Contagem simples
        contagem = {}

        for obra in self.__obras:
            chave = (obra.get_tipo(), obra.get_processo_atual(), obra.get_nome_etapa_atual())
            contagem[chave] = contagem.get(chave, 0) + 1

        print(f"{'TIPO':<25} | {'PROCESSO':<12} | {'ETAPA ATUAL':<25} | QTD")
        print("-" * 70)
        for (tipo, proc, etapa), qtd in sorted(contagem.items()):
            print(f"{tipo:<25} | {proc:<12} | {etapa:<25} | {qtd}")

    # ---------------------------------------------------------
    # Relatório 1: Integrantes do Grupo de Pesquisa
    # ---------------------------------------------------------
    def relatorio_membros(self):
        print("\n=== Relatório 1: Integrantes do Grupo de Pesquisa ===")
        # Ordenar alfabética
        self.__membros.sort(key=lambda x: x.get_nome())
        for m in self.__membros:
            print("-" * 50)
            print(m)