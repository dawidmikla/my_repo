SELECT
    id,
    sum(cnt) as cnt
FROM
    tabela
group by
    id