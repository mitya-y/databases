from postgre_utils import *
from pprint import pprint

execute_query_file("scripts/pets_init/create_tables.sql")
execute_query_file("scripts/pets_init/create_fk.sql")
execute_query_file("scripts/pets_init/fill_tables.sql")
result = execute_query_file("scripts/pets_init/check_pet_table.sql")
pprint(result)
# execute_query_file("scripts/pets_init/delete_tables.sql")
