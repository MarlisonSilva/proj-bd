SELECT nome, dt_nasc
FROM funcionario
WHERE codigo NOT IN (
    SELECT cod_gerente
    FROM departamento
);
