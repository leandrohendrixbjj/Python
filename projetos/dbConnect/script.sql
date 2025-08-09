BEGIN;
-- Deleta a tabela 'pessoa' se ela já existir
DROP TABLE IF EXISTS pessoas ;

-- Cria a tabela 'pessoa' novamente
CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY, -- Campo ID autoincremento
    nome VARCHAR(255) NOT NULL, -- Nome da pessoa
    email VARCHAR(255), -- Email da pessoa, pode ser nulo
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- UTC    
    data_resposta TIMESTAMP WITH TIME ZONE DEFAULT NOW() -- Timezone SP
);

-- Opcional: Inserir uma pessoa de exemplo
INSERT INTO pessoa (nome) VALUES ('Pessoa de Exemplo');

select * from pessoa;

COMMIT;
