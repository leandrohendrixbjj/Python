BEGIN;
-- Deleta a tabela 'pessoa' se ela já existir
DROP TABLE IF EXISTS pessoas ;
DROP TABLE IF EXISTS nota_fiscal;

-- Cria a tabela 'pessoa' novamente
CREATE TABLE pessoas (
    pessoa_id SERIAL PRIMARY KEY, -- Campo ID autoincremento
    nome VARCHAR(255) NOT NULL, -- Nome da pessoa
    email VARCHAR(255), -- Email da pessoa, pode ser nulo
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- UTC    
    data_resposta TIMESTAMP WITH TIME ZONE DEFAULT NOW() -- Timezone SP
);

CREATE TABLE nota_fiscal (
    nota_fiscal_id SERIAL PRIMARY KEY,
    numero VARCHAR(50) NOT NULL,
    data_emissao TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    total NUMERIC(12, 2) NOT NULL,
    pessoa_id INTEGER NOT NULL,
    CONSTRAINT fk_pessoa
      FOREIGN KEY(pessoa_id) REFERENCES pessoas(pessoa_id)
      ON DELETE CASCADE
);

-- Pessoa
INSERT INTO pessoas (nome) VALUES ('Pessoa de Exemplo');

-- Pessoa
INSERT INTO nota_fiscal (numero,total) VALUES (1,100);


COMMIT;
