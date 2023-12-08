#!/usr/bin/env python
# coding: utf-8

# Estrutura de arquivos:
# 
# ```
# .
# ..
# Tratamento_DataSet_atualizado.ipynb
# content/
#     Dados_Censo_PopRua_2020.xlsx
#     csvs (futuros)
# ```

# ## Ajeitando o Banco de Dados:

# In[1]:


# import pandas as pd


# In[2]:


# df = pd.read_excel('content/Dados_Censo_PopRua_2020.xlsx')


# In[3]:


# df.info()


# ## Pessoa

# In[4]:


# Criação da Tabela de Pessoa
# Pessoa = df.loc[:, ['ID', 'Faixa_etaria', 'Idade', 'Sexo', 'Genero', 'Cor_raca', 'Residencia_fixa', 'Tempo_rua_RJ', 'Voltar_cidade_natal']]

# print(Pessoa.head())


# ## Documentos / possui

# In[28]:


# Criar um dicionário de mapeamento de documentos para códigos
# mapeamento_documentos = {
#     'Documento_CPF': 'DOC1',
#     'Documento_Certidao_de_Nascimento': 'DOC2',
#     'Documento_Carteira_de_Identidade': 'DOC3',
#     'Documento_Carteira_de_Trabalho': 'DOC4',
#     'Documento_Titulo_de_Eleitor': 'DOC5'
# }
#
# # Criar uma lista para armazenar as linhas resultantes da tabela Documentos
# linhas_documentos = []
#
# # Iterar sobre cada tipo de documento
# for documento, codigo in mapeamento_documentos.items():
#     linhas_documentos.append({'codigo': f'codigo_{codigo}', 'tipo_documento': documento})
#
# # Criar a tabela Documentos
# Documentos = pd.DataFrame(linhas_documentos)
#
# # Criar uma lista para armazenar as linhas resultantes da tabela Possui
# linhas_possui = []
#
# # Iterar sobre cada linha do DataFrame original
# for _, row in df.iterrows():
#     morador_id = row['ID']  # Supondo que 'ID' é a chave primária da tabela principal
#
#     # Iterar sobre cada tipo de documento
#     for documento, codigo in mapeamento_documentos.items():
#         resposta_documento = row[documento]
#         if resposta_documento.lower() in ['tenho']:
#             linhas_possui.append({'morador_id': morador_id, 'codigo': f'codigo_{codigo}'})
#
# # Criar a tabela Possui
# possui = pd.DataFrame(linhas_possui)
#
# print("Tabela Documentos:")
# print(Documentos)
#
# print("\nTabela Possui:")
# print(possui)
#
#
# # ## Saúde / estado_de
#
# # In[6]:
#
#
# # Criar um dicionário de mapeamento de doenças para códigos
# mapeamento_doencas = {
#     'Diabetes': 'D1',
#     'Pressao_alta': 'D2',
#     'HIV_AIDS': 'D3',
#     'Sifilis_ou_ISTs': 'D4',
#     'Asma_Bronq_Pneum': 'D5',
#     'Tuberculose': 'D6',
#     'Cancer_Tumores': 'D7',
#     'Hepatite': 'D8',
#     'Mental_Epilepsia': 'D9',
#     'Lepra_outras': 'D10',
#     'Infeccao_Urinaria': 'D11',
#     'Ferim_frat_outros': 'D12'
# }
#
# # Criar uma lista para armazenar as linhas resultantes da tabela Saude
# linhas_saude = []
#
# # Iterar sobre cada condição de saúde
# for doenca, codigo in mapeamento_doencas.items():
#     linhas_saude.append({'codigo': f'codigo_{codigo}', 'condicao': f'Problema_Saude_{doenca}'})
#
# # Adicionar a condição de gravidez na tabela Saude
# linhas_saude.append({'codigo': 'codigo_gravidez', 'condicao': 'Gravidez'})
#
# # Criar a tabela Saude
# Saude = pd.DataFrame(linhas_saude)
#
# # Criar uma lista para armazenar as linhas resultantes da tabela estado_de
# linhas_estado_de = []
#
# # Iterar sobre cada linha do DataFrame original
# for _, row in df.iterrows():
#     morador_id = row['ID']  # Supondo que 'ID' é a chave primária da tabela principal
#
#     # Iterar sobre cada condição de saúde
#     for doenca, codigo in mapeamento_doencas.items():
#         resposta_doenca = row[f'Problema_Saude_{doenca}']
#         if resposta_doenca.lower() in ['sim']:
#             linhas_estado_de.append({'ID': morador_id, 'codigo': f'codigo_{codigo}'})
#
#     # Adicionar a condição de gravidez
#     resposta_gravidez = row['Gravidez']
#     if resposta_gravidez.lower() in ['sim']:
#         linhas_estado_de.append({'ID': morador_id, 'codigo': 'codigo_gravidez'})
#
# # Criar a tabela estado_de
# estado_de = pd.DataFrame(linhas_estado_de)
#
# print("Tabela Saude:")
# print(Saude)
#
# print("\nTabela estado_de:")
# print(estado_de)
#
#
# # ## Drogas / faz_uso
#
# # In[7]:
#
#
# # Criar um dicionário de mapeamento de drogas para códigos
# mapeamento_drogas = {
#     'Tabaco': 'DROGA1',
#     'Alcool': 'DROGA2',
#     'Maconha_Haxixe': 'DROGA3',
#     'Crack_Similares': 'DROGA4',
#     'Cocaina': 'DROGA5',
#     'Inalan_Cola_Solven_Tiner': 'DROGA6',
# }
#
# # Criar uma lista para armazenar as linhas resultantes da tabela Drogas
# linhas_drogas = []
#
# # Iterar sobre cada tipo de droga
# for droga, codigo in mapeamento_drogas.items():
#     linhas_drogas.append({'codigo': f'codigo_{codigo}', 'tipo_droga': f'Drogas_{droga}'})
# # Criar a tabela Drogas
# Drogas = pd.DataFrame(linhas_drogas)
#
# # Criar uma lista para armazenar as linhas resultantes da tabela Faz_Uso
# linhas_faz_uso = []
#
# # Iterar sobre cada linha do DataFrame original
# for _, row in df.iterrows():
#     morador_id = row['ID']
#
#     # Iterar sobre cada tipo de droga
#     for droga, codigo in mapeamento_drogas.items():
#         resposta_droga = row[f'Drogas_{droga}']
#         if resposta_droga.lower() in ['sim']:
#             linhas_faz_uso.append({'ID': morador_id, 'codigo': f'codigo_{codigo}'})
#
# # Criar a tabela Faz_Uso
# faz_uso = pd.DataFrame(linhas_faz_uso)
#
# print("Tabela Drogas:")
# print(Drogas)
#
# print("\nTabela Faz_Uso:")
# print(faz_uso)
#
#
# # ## SituacaoRua / vive
#
# # In[8]:
#
#
# # Criar uma lista para armazenar as linhas resultantes da tabela SituacaoRua
# linhas_situacao_rua = []
#
# # Iterar sobre cada linha do DataFrame original
# for _, row in df.iterrows():
#     morador_id = row['ID']  # Supondo que 'ID' é a chave primária da tabela principal
#
#     # Adicionar a situação de rua
#     rua_acolhimento = row['Rua_Acolhimento']
#     motivo_dormir_rua = row['Motivo_dormir_rua']
#
#     linhas_situacao_rua.append({'ID': morador_id, 'Rua_Acolhimento': rua_acolhimento, 'Motivo_dormir_rua': motivo_dormir_rua})
#
# # Criar a tabela SituacaoRua
# SituacaoRua = pd.DataFrame(linhas_situacao_rua)
#
# # Criar uma lista para armazenar as linhas resultantes da tabela vive
# linhas_vive = []
#
# # Iterar sobre cada linha do DataFrame original
# for _, row in df.iterrows():
#     morador_id = row['ID']  # Supondo que 'ID' é a chave primária da tabela principal
#
#     # Adicionar a relação de viver na rua ou abrigado
#     situacao_rua = row['Rua_Acolhimento']
#
#     if situacao_rua.lower() == 'rua':
#         linhas_vive.append({'ID': morador_id, 'SituacaoRua': 'Rua'})
#     elif situacao_rua.lower() == 'acolhidos':
#         linhas_vive.append({'ID': morador_id, 'SituacaoRua': 'Acolhidos'})
#
# # Criar a tabela vive
# vive_em = pd.DataFrame(linhas_vive)
#
# print("Tabela SituacaoRua:")
# print(SituacaoRua)
#
# print("\nTabela vive:")
# print(vive_em)
#
#
# # ## Coleta / realizou_se / Bairro
#
# # In[9]:
#
#
# from datetime import datetime
#
#
# # In[10]:
#
#
# # Criar uma lista para armazenar as linhas resultantes da tabela coleta
# linhas_coleta = []
#
# # Criar uma lista para armazenar as linhas resultantes da tabela bairro
# linhas_bairro = []
#
# # Iterar sobre cada linha do DataFrame original
# for _, row in df.iterrows():
#     morador_id = row['ID']  # Supondo que 'ID' é a chave primária da tabela principal
#     turno = row['Turno']  # Supondo que 'Turno' é a coluna que armazena o turno da coleta
#     codigo_bairro_ra = row['Codigo_da_RA']  # Supondo que 'Codigo_da_RA' é a coluna que armazena o código da RA
#     local_coleta = row['Local_da_coleta_de_dados']  # Supondo que 'Local_da_coleta_de_dados' é a coluna que armazena o local da coleta
#     nome_bairro = row['Bairro'] #MUDEI ISSO AQUIIIIIIIII
#
#
#     # Adicionar informações à tabela coleta
# #    linhas_coleta.append({'ID': morador_id, 'Data': data, 'Turno': turno, 'Codigo_da_RA': codigo_bairro_ra})
#     linhas_coleta.append({'ID': morador_id, 'Turno': turno, 'Codigo_da_RA': codigo_bairro_ra})
#
#     # Adicionar informações à tabela bairro
#     linhas_bairro.append({'nome_bairro': nome_bairro, 'Codigo_da_RA': codigo_bairro_ra}) #MUDEI ISSO AQUIIIIIIIIIII
#
# # Criar a tabela coleta
# coleta = pd.DataFrame(linhas_coleta)
#
# # Criar a tabela bairro
# bairro = pd.DataFrame(linhas_bairro).drop_duplicates()
#
# # Criar a tabela realizou_se
# realizou_se = pd.merge(coleta, bairro, left_on='Codigo_da_RA', right_on='Codigo_da_RA', how='inner').drop(columns=['Turno'])
#
# print("Tabela coleta:")
# print(coleta)
#
# print("\nTabela bairro:")
# print(bairro)
#
# print("\nTabela realizou_se:")
# print(realizou_se)


# # Tentando baixar as tabelas criadas no PC:

# In[11]:


caminho = 'content/'

# dePara com nome da tabela no sql -- nome do csv correspondente
tabela_arquivo = {'Pessoa' : 'Pessoa.csv',
                  'Documentos': 'Documentos.csv', 
                  'possui': 'possui.csv',
                  'SituacaoRua': 'SituacaoRua.csv',
                  'vive': 'vive.csv',
                  'Drogas': 'Drogas.csv',
                  'Saude': 'Saude.csv',
                  'bairro': 'bairro.csv',
                  'coleta': 'coleta.csv',
                  'estado_de': 'estado_de.csv',
                  'faz_uso': 'faz_uso.csv',
                  'realizou_se': 'realizou_se.csv'
                 }


# In[12]:


# Pessoa.to_csv(caminho + tabela_arquivo['Pessoa'], index=False)
# Documentos.to_csv(caminho + tabela_arquivo['Documentos'], index=False)
# possui.to_csv(caminho + tabela_arquivo['possui'], index=False)
# vive_em.to_csv(caminho + tabela_arquivo['vive'], index=False)
# SituacaoRua.to_csv(caminho + tabela_arquivo['SituacaoRua'], index=False)
# Drogas.to_csv(caminho + tabela_arquivo['Drogas'], index=False)
# Saude.to_csv(caminho + tabela_arquivo['Saude'], index=False)
# bairro.to_csv(caminho + tabela_arquivo['bairro'], index=False)
# coleta.to_csv(caminho + tabela_arquivo['coleta'], index=False)
# estado_de.to_csv(caminho + tabela_arquivo['estado_de'], index=False)
# faz_uso.to_csv(caminho + tabela_arquivo['faz_uso'], index=False)
# realizou_se.to_csv(caminho + tabela_arquivo['realizou_se'], index=False)

# from google.colab import files

# files.download('Pessoa.csv')
# files.download('Documentos.csv')
# files.download('possui.csv')
# files.download('vive.csv')
# files.download('SituacaoRua.csv')
# files.downloa': 5393d('Drogas.csv')
# files.download('Saude.csv')
# files.download('bairro.csv')
# files.download('coleta.csv')
# files.download('estado_de.csv')
# files.download('faz_uso.csv')
# files.download('realizou_se.csv')


# ### Criando o Arquivo SQL

# In[22]:


# script_sql = """
# -- Criação da tabela Pessoa
# CREATE TABLE Pessoa (
#     ID INT PRIMARY KEY,
#     Faixa_etaria VARCHAR(255),
#     Idade INT,
#     Sexo VARCHAR(255),
#     Genero VARCHAR(255),
#     Cor_raca VARCHAR(255),
#     Residencia_fixa VARCHAR(255),
#     Tempo_rua_RJ VARCHAR(255),
#     Voltar_cidade_natal VARCHAR(255)
# );
#
# -- Criação da tabela Documentos
# CREATE TABLE Documentos (
#     codigo VARCHAR(255) PRIMARY KEY,
#     tipo_documento VARCHAR(255) NOT NULL
# );
#
# -- Criação da tabela possui
# CREATE TABLE possui (
#     morador_id INT,
#     codigo VARCHAR(255),
#     FOREIGN KEY (codigo) REFERENCES Documentos(codigo),
#     PRIMARY KEY (morador_id, codigo)
# );
#
# -- Criação da tabela Saude
# CREATE TABLE Saude (
#     codigo VARCHAR(255) PRIMARY KEY,
#     condicao VARCHAR(255) NOT NULL
# );
#
# -- Criação da tabela estado_de
# CREATE TABLE estado_de (
#     ID INT,
#     codigo VARCHAR(255),
#     FOREIGN KEY (codigo) REFERENCES Saude(codigo),
#     PRIMARY KEY (ID, codigo)
# );
#
# -- Criação da tabela Drogas
# CREATE TABLE Drogas (
#     codigo VARCHAR(255) PRIMARY KEY,
#     tipo_droga VARCHAR(255) NOT NULL
# );
#
# -- Criação da tabela faz_uso
# CREATE TABLE faz_uso (
#     ID INT,
#     codigo VARCHAR(255),
#     FOREIGN KEY (codigo) REFERENCES Drogas(codigo),
#     PRIMARY KEY (ID, codigo)
# );
#
# -- Criação da Tabela SituacaoRua
# CREATE TABLE SituacaoRua (
#     ID INT PRIMARY KEY,
#     Rua_Acolhimento VARCHAR(255),
#     Motivo_dormir_rua VARCHAR(500)
# );
#
# -- Criação da Tabela vive
# CREATE TABLE vive (
#     ID INT PRIMARY KEY,
#     SituacaoRua VARCHAR(255),
#     FOREIGN KEY (ID) REFERENCES SituacaoRua(ID)
# );
#
# -- Criação da Tabela bairro
# CREATE TABLE bairro (
#     Codigo_da_RA INT,
#     nome_bairro VARCHAR(255), 
#     PRIMARY KEY (Codigo_da_RA, nome_bairro)
# );
#
# -- Criação da Tabela coleta
# CREATE TABLE coleta (
#     ID INT PRIMARY KEY,
#     -- Data DATE,
#     Turno VARCHAR(255),
#     Codigo_da_RA INT,
#     FOREIGN KEY (Codigo_da_RA) REFERENCES bairro(Codigo_da_RA)
# );
#
# -- Criação da Tabela realizou_se
# CREATE TABLE realizou_se (
#     ID INT,
#     nome_bairro VARCHAR(255),
#     Codigo_da_RA INT,
#     FOREIGN KEY (ID) REFERENCES coleta(ID),
#     FOREIGN KEY (Codigo_da_RA) REFERENCES bairro(Codigo_da_RA),
#     PRIMARY KEY(ID, nome_bairro, Codigo_da_RA)
# );
# """
#
# # Escrever o script no arquivo
# with open("popRua.sql", "w") as arquivo:
#     arquivo.write(script_sql)
#
# print("Script salvo com sucesso!")


# ### Criando a Database e Populando
# 
# Instalem pandas (eu instalei pelo terminal usando `pip3 install pandas`) e esse sqlalchemy também das mesma forma)
# 
# OBS: UM ERRO QUE EU TIVE FOI QUE MEU USUÁRIO TAVA SEM PRIVILÉGIO P/ INSERIR NAS TABELAS DA DATABASE, POR ALGUM MOTIVO... ENTÃO DEÊM O GRANT INSERT ON...

# In[23]:


import pandas as pd
# import mysql.connector
from sqlalchemy import create_engine

# Substitua 'seu_usuario', 'sua_senha', 'seu_host' e 'seu_banco' com suas credenciais e configurações
usuario = 'root' # seu usuário
senha = 'senha' # sua senha
host = 'localhost'
NOME_DB = 'popRua' # esse foi o nome que eu dei aqui no meu


# Crie a conexão com o MySQL
conn = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{NOME_DB}')


# Limpa a instalação:

# In[24]:


# clean install
# conn.execute("DROP DATABASE IF EXISTS " + NOME_DB)
#
# conn.execute("CREATE DATABASE IF NOT EXISTS " + NOME_DB)
#
# print("Limpeza executada!")


# Cria as tabelas a partir do arquivo .sql com os comandos

# In[25]:


# Ler o conteúdo do arquivo .sql
# with open('popRua.sql', 'r') as file:
#     sql_commands = file.read()
#
# # Dividir os comandos SQL em instruções individuais
# commands = sql_commands.split(';')
#
# # Conectar ao banco de dados e executar os comandos
# with conn.connect() as connection:
#     # Selecionar a base de dados
#     connection.execute(f"USE {NOME_DB}")
#
#     for command in commands:
#         if command.strip():  # Ignorar linhas em branco
#             connection.execute(command)
#
# print("Tabelas criadas com sucesso!")


# Populando popRua com os dados do CSV.

# In[26]:


for nomeTabela, arquivo in tabela_arquivo.items():  
    # Caminho para o arquivo CSV
    caminho_csv = caminho + arquivo

    # Ler o arquivo CSV usando o pandas
    tabela = pd.read_csv(caminho_csv)

    # Inserir dados na tabela do MySQL
    tabela.to_sql(nomeTabela, con=conn, if_exists='append', index=False)
    
    print(f"Populada {nomeTabela} com sucesso!")
