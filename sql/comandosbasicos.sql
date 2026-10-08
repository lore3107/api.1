#consultasql
select field1
from table
where field = condition;

#cláusulaselect
select field1 
"identifica a coluna que vc deseja extrair os dados"
  caso usar select * estaria selecionando todas as colunas da tabela, ao invés de apenas a coluna field1

#cláusulafrom
from table
"identifica onde a coluna está localizada"

#cláusulawhere
where field = 'Chavez'
"restringe somente os dados com determinada condição"

#fazercomentários
/* this is the last name column */
-- this is the customer data table
SELECT
	field1 /* this is the last name column */
FROM
	table -- this is the customer data table  
WHERE
	field1 = 'Chavez';
