from postgre_utils import execute_query_file

execute_query_file("scripts/bank/create.sql")
execute_query_file("scripts/bank/add_fk.sql")
execute_query_file("scripts/bank/fill.sql")
execute_query_file("scripts/bank/delete.sql")

