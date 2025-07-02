
-- Query de consulta de projetos e atividades
SELECT 
    p.codigo AS codigo_projeto,
    p.nome AS nome_projeto,
    p.descricao AS descricao_projeto,
    a.codigo AS codigo_atividade,
    a.descricao AS descricao_atividade,
    a.data_inicio AS inicio_atividade,
    a.data_fim AS fim_atividade
FROM 
    projeto p
LEFT JOIN 
    atividade a ON p.codigo = a.projeto
ORDER BY 
    p.codigo, a.codigo;

-- update responsável projeto
UPDATE projeto
SET responsavel = 2
WHERE codigo = 1;

-- update atividade 
INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
VALUES ('Criar layout da interface', 1, '2025-01-15', '2025-01-31');