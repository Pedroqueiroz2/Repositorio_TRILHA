import json
from itertools import chain 

with open("movies_and_series.json", "r") as arquivo:
    dados = json.load(arquivo)

    filmes = dados["data"]["movies"]
    series = dados["data"]["series"]

    tudo = list(chain(filmes,series))

    #Questão 1
titulos_filmes = []
for filme in filmes:
    titulos_filmes.append(filme["title"])

    #Questão 2
    titulos_series = []
for serie in series:
    titulos_series.append(serie["title"])

    #Questão 3
    avaliacao = -10

    for indice in tudo:
        if(indice.get("rating") > avaliacao):
            avaliacao = indice.get("rating")
            nome_maior = indice.get("title")

    #Questão 4
    generos_filmes_series = []
for genero_filmes in filmes:
    generos_filmes_series.extend(genero_filmes["genres"])

for genero_series in series:
    generos_filmes_series.extend(genero_series["genres"])

lista_de_generos = set(generos_filmes_series)

    #Questão 5
total_filmes = len(filmes)
total_series = len(series)

    #Questão 6
plataformas_streaming = []
for streaming_filmes in filmes:
    plataformas_streaming.extend(streaming_filmes["streaming"])

for streaming_series in series:
    plataformas_streaming.extend(streaming_series["streaming"])

    plataformas = set(plataformas_streaming)

    #Questão 7
    resolucao_filmes_series = []
for filme in filmes:
    if "Netflix" in filme["streaming"]:
        if "4K" in filme["streaming"]["Netflix"]["resolution"]:
            resolucao_filmes_series.append(filme["title"])

for serie in series:
    if "Netflix" in serie["streaming"]:
        if "4K" in serie["streaming"]["Netflix"]["resolution"]:
            resolucao_filmes_series.append(serie["title"])

    #Questão 8
    filme_escolhido = "The Shawshank Redemption"
    plataformas_disponiveis = []
    urls_disponiveis = []

    for filme in filmes:
        if filme["title"] == filme_escolhido:
            if "streaming" in filme:
                for plataforma, detalhes in filme["streaming"].items():
                    if detalhes.get("available", False):
                        plataformas_disponiveis.append(plataforma)
    for f in filmes:
        for keys, values in f["streaming"].items():
            urls_disponiveis.append(f["streaming"]["Netflix"]["url"])

        urls_disponiveis.append(f["streaming"]["Amazon Prime"]["url"])
        url_final = set(urls_disponiveis)

    #Questão 9
atores_personagens = []
for item in tudo:
        if "cast" in item:
            for ator in item["cast"]:
                atores_personagens.append({
                "ator": ator.get("actor", "Desconhecido"),
                "personagem": ator.get("character", "Desconhecido")
})
                
    #Questão 10
ator_maior_salario = []
maior_salario = 0
for item in tudo:
        if "cast" in item:
            for ator in item["cast"]:
                salario = ator.get("salary", 0)
                if salario > maior_salario:
                    maior_salario = salario
                    ator_maior_salario = ator["actor"]
            
    #Questão 11
locais_filmes = []
for filme in filmes:
    if "filmingLocations" in filme["production"]:
        locais_filmes.append(filme["production"]["filmingLocations"])

    #Questão 12
lista_diretores = []
for filme in filmes:
    lista_diretores.append(filme["directors"])

    #Questão 13
filme_maior_receita = None
maior_receita = 0
for filme in filmes:
    if "boxOffice" in filme["production"]:
        receita = filme["production"]["boxOffice"]["revenue"]
        if receita > maior_receita:
            maior_receita = receita
            filme_maior_receita = filme["title"]

    #Questão 14 
lucro = []
lucro_filme = 0
for filme in filmes:
    if "boxOffice" in filme["production"]:
        lucro_filme = filme["production"]["boxOffice"]["profit"]
    lucro.append(lucro_filme)
    if lucro: 
        lucro_medio = sum(lucro) / len(lucro)

        #Questão 15
ingressos = []
for f in filmes:
    for keys, values in f["production"].items():
        ingressos.append(f["production"]["boxOffice"]["ticketSales"]["domestic"])
for f in filmes:
    for keys, values in f["production"].items():
        ingressos.append(f["production"]["boxOffice"]["ticketSales"]["international"])
ingresos_orga = set(ingressos)

#Questão 16
premios = []

for f in tudo:
    for premio in f["awards"]:
        premio_filtrado = {
            chave: valor for chave, valor in premio.items() 
            if chave not in ["won", "nominees"]
        }
        premios.append(premio_filtrado)

    #Questão 17
filmes_series_premiados = []
for f in filmes:
    for premiados in f["awards"]:
        if  premiados.get("won", False):
            filmes_series_premiados.append(f["title"])
for s in series:
    for premiados in s["awards"]:
        if  premiados.get("won", True):
            filmes_series_premiados.append(s["title"])

#Questão 18
indicados_por_ano = {}
indicados_ano = []

for filme in filmes:
    if "awards" in filme:
        for premio in filme["awards"]:
            if premio.get("category") == "Best Picture":
                ano = premio["year"]
                nomeados = premio["nominees"]

                if ano not in indicados_por_ano:
                    indicados_por_ano[ano] = []
                indicados_por_ano[ano].extend(nomeados)
for ano, nomeados in indicados_por_ano.items():
    indicados_ano.append(ano)
    indicados_ano.append(nomeados)

    #Questão 19
mais_votado = []
votos = -1

if "reviews" in item:
    for review in item["reviews"]:
        votos_atuais = review["details"]["helpfulVotes"]
        if votos_atuais > votos:
             votos = votos_atuais  
mais_votado = review["comment"]  

#Questão 20
notas = []
for f in filmes:
    notas.append(f["rating"])
soma = sum(notas)
media = soma / len(notas)

#Quest.21
avaliacoes_antes_2022 = []
for filme in filmes:
    for avaliacao in filme['reviews']:
        data_avaliacao = avaliacao['details']['date']
        ano = int(data_avaliacao.split('-')[0])
        if ano < 2022:
            avaliacoes_antes_2022.append(filme["reviews"])

for serie in dados['data']['series']:
    for avaliacao in serie['reviews']:
        data_avaliacao = avaliacao['details']['date']
        ano = int(data_avaliacao.split('-')[0])
        if ano < 2022:
            avaliacoes_antes_2022.append(serie["reviews"])

with open("Respostas_TRILHA.txt", "w", encoding="utf-8") as arquivo_txt:
    # Questão 1
    arquivo_txt.write("Questão 1: Listar todos os títulos de filmes\n")
    arquivo_txt.write("\n".join(titulos_filmes) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 2
    arquivo_txt.write("Questão 2: Listar todas as séries\n")
    arquivo_txt.write("\n".join(titulos_series) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 3
    arquivo_txt.write("Questão 3: Recuperar o filme/série com maior nota (rating)\n")
    arquivo_txt.write(f"{nome_maior}\n")
    arquivo_txt.write("============================================\n")

    # Questão 4
    arquivo_txt.write("Questão 4: Listar os gêneros de todos os filmes e séries\n")
    arquivo_txt.write(", ".join(lista_de_generos) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 5
    arquivo_txt.write("Questão 5: Obter o número total de filmes e séries\n")
    arquivo_txt.write(f"Total de filmes: {total_filmes}\n")
    arquivo_txt.write(f"Total de séries: {total_series}\n")
    arquivo_txt.write("============================================\n")

    # Questão 6
    arquivo_txt.write("Questão 6: Listar todas as plataformas de streaming disponíveis\n")
    arquivo_txt.write(", ".join(plataformas) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 7
    arquivo_txt.write("Questão 7: Filtrar os filmes/séries disponíveis em 4K no Netflix\n")
    arquivo_txt.write("\n".join(resolucao_filmes_series) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 8
    arquivo_txt.write("Questão 8: Identificar plataformas onde um filme específico está disponível\n")
    arquivo_txt.write(f"Filme: {filme_escolhido}\n")
    arquivo_txt.write(f"Plataformas disponíveis: {', '.join(plataformas_disponiveis)}\n")
    arquivo_txt.write(f"URLs disponíveis: {', '.join(url_final)}\n")
    arquivo_txt.write("============================================\n")

    # Questão 9
    arquivo_txt.write("Questão 9: Listar todos os atores e os personagens que interpretam\n")
    for ator_personagem in atores_personagens:
        arquivo_txt.write(f"{ator_personagem['ator']} como {ator_personagem['personagem']}\n")
    arquivo_txt.write("============================================\n")

    # Questão 10
    arquivo_txt.write("Questão 10: Obter o ator com maior salário em um filme ou série\n")
    arquivo_txt.write(f"{ator_maior_salario}\n")
    arquivo_txt.write("============================================\n")

    # Questão 11
    arquivo_txt.write("Questão 11: Listar todas as localizações de filmagem dos filmes\n")
    for local in locais_filmes:
        arquivo_txt.write(", ".join(local) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 12
    arquivo_txt.write("Questão 12: Listar os diretores de cada filme\n")
    for diretor in lista_diretores:
        arquivo_txt.write(", ".join(diretor) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 13
    arquivo_txt.write("Questão 13: Obter o filme com maior receita na bilheteria (revenue)\n")
    arquivo_txt.write(f"{filme_maior_receita}\n")
    arquivo_txt.write("============================================\n")

    # Questão 14
    arquivo_txt.write("Questão 14: Calcular o lucro médio dos filmes\n")
    arquivo_txt.write(f"Lucro médio: ${lucro_medio:.2f}\n")
    arquivo_txt.write("============================================\n")

    # Questão 15
    arquivo_txt.write("Questão 15: Obter a distribuição de vendas de ingressos por região\n")
    arquivo_txt.write(f"Vendas domésticas: {ingressos[0]}\n")
    arquivo_txt.write(f"Vendas internacionais: {ingressos[1]}\n")
    arquivo_txt.write("============================================\n")

    # Questão 16
    arquivo_txt.write("Questão 16: Listar todos os prêmios e categorias de cada filme/série\n")
    for premio in premios:
        arquivo_txt.write(f"{premio}\n")
    arquivo_txt.write("============================================\n")

    # Questão 17
    arquivo_txt.write("Questão 17: Identificar filmes/séries que ganharam prêmios\n")
    arquivo_txt.write("\n".join(filmes_series_premiados) + "\n")
    arquivo_txt.write("============================================\n")

    # Questão 18
    arquivo_txt.write("Questão 18: Listar os indicados ao prêmio de 'Melhor Filme' de cada ano\n")
    for ano, nomeados in indicados_por_ano.items():
        arquivo_txt.write(f"Ano: {ano}\n")
        arquivo_txt.write(f"Indicados: {', '.join(nomeados)}\n")
    arquivo_txt.write("============================================\n")

    # Questão 19
    arquivo_txt.write("Questão 19: Obter o comentário com maior número de votos úteis (helpfulVotes)\n")
    arquivo_txt.write(f"{mais_votado}\n")
    arquivo_txt.write("============================================\n")

    # Questão 20
    arquivo_txt.write("Questão 20: Calcular a nota média dos filmes\n")
    arquivo_txt.write(f"Nota média: {media:.2f}\n")
    arquivo_txt.write("============================================\n")

    # Questão 21
    arquivo_txt.write("Questão 21: Filtrar todas as avaliações feitas antes de 2022\n")
    for avaliacao in avaliacoes_antes_2022:
        arquivo_txt.write(f"{avaliacao}\n")
    arquivo_txt.write("============================================\n")
