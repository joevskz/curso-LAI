# main.py
from pesquisador import Pesquisador
from artigo_periodico import ArtigoPeriodico
from artigo_conferencia import ArtigoConferencia
from capitulo_livro import CapituloLivro
from livro_completo import LivroCompleto
from grupo_pesquisa import GrupoPesquisa
from constantes import CANAIS_DIFUSAO


def main():
    sistema = GrupoPesquisa()

    # 1. Cadastro de Pesquisadores
    p1 = Pesquisador("João da Silva", "111.111.111-11", "joao@univ.br", "9999-1111", "lattes.cnpq.br/1", "orcid/1",
                     "Computação", "UFSC", "Docente", "Mesma Instituição")
    p2 = Pesquisador("Maria Souza", "222.222.222-22", "maria@univ.br", "9999-2222", "lattes.cnpq.br/2", "orcid/2",
                     "Computação", "UFSC", "Mestrando", "Mesma Instituição")
    p3 = Pesquisador("Carlos Pereira", "333.333.333-33", "carlos@usp.br", "9999-3333", "lattes.cnpq.br/3", "orcid/3",
                     "Engenharia", "USP", "Docente", "Outra Instituição")
    p4 = Pesquisador("Ana Costa", "444.444.444-44", "ana@univ.br", "9999-4444", "lattes.cnpq.br/4", "orcid/4",
                     "Computação", "UFSC", "Doutorando", "Mesma Instituição")
    p5 = Pesquisador("Pedro Santos", "555.555.555-55", "pedro@indep.org", "9999-5555", "lattes.cnpq.br/5", "orcid/5",
                     "N/A", "Independente", "Voluntário", "Independente")
    p6 = Pesquisador("Lucia Lima", "666.666.666-66", "lucia@univ.br", "9999-6666", "lattes.cnpq.br/6", "orcid/6",
                     "Computação", "UFSC", "Graduando", "Mesma Instituição")

    sistema.adicionar_membro(p1)
    sistema.adicionar_membro(p2)
    sistema.adicionar_membro(p3)
    sistema.adicionar_membro(p4)
    sistema.adicionar_membro(p5)
    sistema.adicionar_membro(p6)

    # 2. Cadastro de Obras Científicas

    # --- GRUPO 1: Produção (Status de 0 a 8) ---
    w1 = ArtigoPeriodico("Uso de IA na Saúde", "IA; Saúde; Python", "Resumo 1", [p1, p2], "Jornal Med", "10", "2",
                         "10-20", "doi/1", 2025, "url1", "SP")
    w1.set_etapa_manual("Produção", 1)  # Curadoria

    w2 = ArtigoConferencia("Redes Neurais em Jogos", "Games; NN; AI", "Resumo 2", [p2, p6], "GameConf", "Rio",
                           "2025-05", "SBC", "Anais Game", "doi/2", 2025, "url2")
    w2.set_etapa_manual("Produção", 4)  # Metodologia

    w3 = LivroCompleto("Introdução a Python", "Python; Ensino", "Resumo 3", [p1], "Novatec", "SP", 2025, "isbn/3",
                       "url3")
    w3.set_etapa_manual("Produção", 7)  # Escrita esboço

    w4 = CapituloLivro("Variáveis em Python", "Var; Code", "Resumo 4", [p1, p4], "Introdução a Python", "Silva, J.",
                       "Novatec", "SP", 2025, "isbn/3", "url4")
    w4.set_etapa_manual("Produção", 8)  # Revisão

    w5 = ArtigoPeriodico("Big Data em Finanças", "Dados; Money", "Resumo 5", [p3, p5], "Finance Journal", "5", "1",
                         "100-110", "doi/5", 2025, "url5", "NY")
    w5.set_etapa_manual("Produção", 0)  # Conceitualização

    w6 = ArtigoConferencia("Robótica Educacional", "Robô; Escola", "Resumo 6", [p6], "EduRobo", "Bahia", "2025-10",
                           "UFSC", "Anais Edu", "doi/6", 2025, "url6")
    w6.set_etapa_manual("Produção", 3)  # Investigação

    # --- GRUPO 2: Publicação (Status de 0 a 7) ---
    w7 = ArtigoPeriodico("Segurança em IoT", "IoT; Sec", "Resumo 7", [p1, p3, p5], "Sec Journal", "2", "2", "30-40",
                         "doi/7", 2024, "url7", "Londres")
    w7.set_etapa_manual("Publicação", 3)  # Submissão

    w8 = ArtigoConferencia("Blockchain Gov", "Block; Gov", "Resumo 8", [p2], "GovTech", "Brasilia", "2024-11", "Gov",
                           "Anais Gov", "doi/8", 2024, "url8")
    w8.set_etapa_manual("Publicação", 5)  # Revisão

    w9 = CapituloLivro("Smart Contracts", "Smart; Code", "Resumo 9", [p2, p3], "Blockchain Book", "Moraes, R.",
                       "Elsevier", "AMS", 2024, "isbn/9", "url9")
    w9.set_etapa_manual("Publicação", 6)  # Resubmissão

    w10 = LivroCompleto("Futuro da Web", "Web; 3.0", "Resumo 10", [p4, p5], "Casa do Código", "SP", 2024, "isbn/10",
                        "url10")
    w10.set_etapa_manual("Publicação", 0)  # Seleção de veículo

    w11 = ArtigoPeriodico("Algoritmos Genéticos", "Gen; Algo", "Resumo 11", [p6, p1], "Evolution Journal", "8", "3",
                          "200-210", "doi/11", 2024, "url11", "Berlim")
    w11.set_etapa_manual("Publicação", 4)  # Correção

    w12 = ArtigoConferencia("Realidade Virtual", "VR; AR", "Resumo 12", [p4], "VR Conf", "Tokio", "2024-12", "IEEE",
                            "Anais VR", "doi/12", 2024, "url12")
    w12.set_etapa_manual("Publicação",
                         7)  # Publicação Final (Já conta como publicado, mas ainda não foi para difusão ativa no sistema)

    # --- GRUPO 3: Difusão ---
    # Nota: set_etapa_manual("Difusão", 0) configura o estado macro para Difusão

    w13 = ArtigoPeriodico("Vacinas mRNA", "Bio; Tech", "Resumo 13", [p1, p5], "Nature", "99", "1", "1-5", "10.1038/x",
                          2023, "url13", "UK")
    w13.set_etapa_manual("Difusão", 0)
    w13.set_status_difusao_canal("X-Twitter", 5)  # Divulgação (Final)
    w13.set_status_difusao_canal("Instagram", 1)  # Ilustração

    w14 = LivroCompleto("História da Computação", "Hist; Comp", "Resumo 14", [p3], "Editora A", "RJ", 2022, "978-85",
                        "url14")
    w14.set_etapa_manual("Difusão", 0)
    w14.set_status_difusao_canal("Blog/Web", 3)  # Adaptação

    w15 = ArtigoConferencia("Cloud Computing", "AWS; Azure", "Resumo 15", [p2, p4], "CloudConf", "USA", "2023-01",
                            "ACM", "Proc Cloud", "10.1145/y", 2023, "url15")
    w15.set_etapa_manual("Difusão", 0)
    w15.set_status_difusao_canal("Youtube", 4)  # Prod Multimídia

    w16 = CapituloLivro("Serverless", "Func; Cloud", "Resumo 16", [p2], "Cloud Patterns", "Author, A", "OReilly", "US",
                        2023, "isbn/16", "url16")
    w16.set_etapa_manual("Difusão", 0)
    # Nenhum progresso específico, apenas entrou em difusão (tudo 0)

    w17 = ArtigoPeriodico("Educação a Distância", "EAD; Covid", "Resumo 17", [p1, p6], "Edu Journal", "4", "1", "50-60",
                          "doi/17", 2022, "url17", "Lisboa")
    w17.set_etapa_manual("Difusão", 0)
    w17.set_status_difusao_canal("WhatsApp/Telegram", 5)

    w18 = ArtigoConferencia("Agile Scrum", "Agile; Soft", "Resumo 18", [p5], "Agile Brazil", "POA", "2022-09",
                            "AgileAll", "Anais Agile", "doi/18", 2022, "url18")
    w18.set_etapa_manual("Difusão", 0)
    w18.set_status_difusao_canal("Reddit", 2)  # Diagramação

    # Adicionando ao sistema
    obras = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18]
    for obra in obras:
        sistema.adicionar_obra(obra)

    # 3. Gerar Relatórios
    sistema.relatorio_membros()
    sistema.relatorio_portfolio()
    sistema.relatorio_disseminacao()
    sistema.relatorio_difusao()
    sistema.relatorio_produtividade()


if __name__ == "__main__":
    main()