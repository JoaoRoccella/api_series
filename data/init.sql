-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS api_series;
USE api_series;

-- Criar a tabela de séries
CREATE TABLE IF NOT EXISTS serie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    ano_lancamento INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Opcional: Popular com alguns dados iniciais
INSERT INTO serie (titulo, descricao, ano_lancamento) VALUES 
('Breaking Bad', 'Um professor de química se torna traficante.', 2008),
('Succession', 'A disputa de poder em um império de mídia.', 2018),
('Dark', 'Série de ficção científica alemã sobre viagens no tempo.', 2017);