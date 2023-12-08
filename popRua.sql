
-- Criação da tabela Pessoa
CREATE TABLE Pessoa (
    ID INT PRIMARY KEY,
    Faixa_etaria VARCHAR(255),
    Idade INT,
    Sexo VARCHAR(255),
    Genero VARCHAR(255),
    Cor_raca VARCHAR(255),
    Residencia_fixa VARCHAR(255),
    Tempo_rua_RJ VARCHAR(255),
    Voltar_cidade_natal VARCHAR(255)
);

-- Criação da tabela Documentos
CREATE TABLE Documentos (
    codigo VARCHAR(255) PRIMARY KEY,
    tipo_documento VARCHAR(255) NOT NULL
);

-- Criação da tabela possui
CREATE TABLE possui (
    morador_id INT,
    codigo VARCHAR(255),
    FOREIGN KEY (codigo) REFERENCES Documentos(codigo),
    PRIMARY KEY (morador_id, codigo)
);

-- Criação da tabela Saude
CREATE TABLE Saude (
    codigo VARCHAR(255) PRIMARY KEY,
    condicao VARCHAR(255) NOT NULL
);

-- Criação da tabela estado_de
CREATE TABLE estado_de (
    ID INT,
    codigo VARCHAR(255),
    FOREIGN KEY (codigo) REFERENCES Saude(codigo),
    PRIMARY KEY (ID, codigo)
);

-- Criação da tabela Drogas
CREATE TABLE Drogas (
    codigo VARCHAR(255) PRIMARY KEY,
    tipo_droga VARCHAR(255) NOT NULL
);

-- Criação da tabela faz_uso
CREATE TABLE faz_uso (
    ID INT,
    codigo VARCHAR(255),
    FOREIGN KEY (codigo) REFERENCES Drogas(codigo),
    PRIMARY KEY (ID, codigo)
);

-- Criação da Tabela SituacaoRua
CREATE TABLE SituacaoRua (
    ID INT PRIMARY KEY,
    Rua_Acolhimento VARCHAR(255),
    Motivo_dormir_rua VARCHAR(500)
);

-- Criação da Tabela vive
CREATE TABLE vive (
    ID INT PRIMARY KEY,
    SituacaoRua VARCHAR(255),
    FOREIGN KEY (ID) REFERENCES SituacaoRua(ID)
);

-- Criação da Tabela bairro
CREATE TABLE bairro (
    Codigo_da_RA INT,
    nome_bairro VARCHAR(255), 
    PRIMARY KEY (Codigo_da_RA, nome_bairro)
);

-- Criação da Tabela coleta
CREATE TABLE coleta (
    ID INT PRIMARY KEY,
    -- Data DATE,
    Turno VARCHAR(255),
    Codigo_da_RA INT,
    FOREIGN KEY (Codigo_da_RA) REFERENCES bairro(Codigo_da_RA)
);

-- Criação da Tabela realizou_se
CREATE TABLE realizou_se (
    ID INT,
    nome_bairro VARCHAR(255),
    Codigo_da_RA INT,
    FOREIGN KEY (ID) REFERENCES coleta(ID),
    FOREIGN KEY (Codigo_da_RA) REFERENCES bairro(Codigo_da_RA),
    PRIMARY KEY(ID, nome_bairro, Codigo_da_RA)
);
