from postgre_utils import *
from pprint import pprint

execute_query_file("scripts/pets_vacine/clear.sql")
# execute_query_file("scripts/pets_vacine/clear.sql")
execute_query_file("scripts/pets_init/all.sql")
execute_query_file("scripts/pets_vacine/add_vacines.sql")

exit()
result = execute_query("SELECT * FROM Pet WHERE Nick = 'Partizan';")
pprint(result)

result = execute_query("SELECT Nick, Breed, Age FROM Pet ORDER BY Age;")
pprint(result)

result = execute_query("SELECT * FROM Pet WHERE Description IS NOT NULL AND Description NOT LIKE '';")
pprint(result)

result = execute_query("SELECT AVG(Age) FROM Pet WHERE breed = 'poodle';")
print(result[0][0])

result = execute_query("SELECT Pet WHERE breed = 'poodle';")
print(result[0][0])
