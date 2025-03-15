from postgre_utils import *
from pprint import pprint

execute_query_file("scripts/pets_vacine/clear.sql")
execute_query_file("scripts/pets_vacine/all.sql")
