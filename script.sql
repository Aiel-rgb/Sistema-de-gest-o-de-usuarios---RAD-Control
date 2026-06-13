CREATE DATABASE rad_db;

\c rad_db

CREATE TABLE IF NOT EXISTS solicitacoes (
    id               SERIAL PRIMARY KEY,
    aluno_nome       VARCHAR(120)  NOT NULL,
    matricula        VARCHAR(30)   NOT NULL,
    tipo             VARCHAR(40)   NOT NULL,
    prioridade       VARCHAR(20)   NOT NULL,
    status           VARCHAR(25)   NOT NULL,
    descricao        TEXT          NOT NULL,
    data_abertura    TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
    prazo            DATE
);