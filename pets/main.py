from postgre_utils import *
from pprint import pprint

# execute_query_file("scripts/pets_vacine/clear.sql")
# execute_query_file("scripts/pets_vacine/old_bd.sql")
# execute_query_file("scripts/pets_vacine/add_vacines.sql")

def select_part1():
    print("select 1")
    result = execute_query("SELECT * FROM Pet WHERE Nick = 'Partizan';")
    pprint(result)
    
    print("select 2")
    result = execute_query("SELECT Nick, Breed, Age FROM Pet ORDER BY Age;")
    pprint(result)
    
    print("select 3")
    result = execute_query("SELECT * FROM Pet WHERE Description IS NOT NULL AND Description NOT LIKE '';")
    pprint(result)
    
    print("select 4")
    result = execute_query("SELECT AVG(Age) FROM Pet WHERE breed = 'poodle';")
    pprint(result[0][0])
    
    print("select 5")
    result = execute_query("SELECT COUNT(DISTINCT Owner_ID) FROM Pet;")
    pprint(result[0][0])
    
    print("select 6")
    result = execute_query("SELECT Breed, COUNT(*) FROM Pet GROUP BY Breed;")
    pprint(result)
    
    print("select 7")
    result = execute_query("SELECT Breed, COUNT(*) FROM Pet GROUP BY Breed HAVING COUNT(*) > 1;")
    pprint(result)
    
    print("select 8")
    result = execute_query("SELECT * FROM Pet WHERE Age BETWEEN 5 AND 10;")
    pprint(result)
    
    print("select 9")
    result = execute_query("SELECT * FROM Pet WHERE Age BETWEEN 5 AND 10;")
    pprint(result)

    print("select 10")
    result = execute_query("SELECT * FROM Pet WHERE Breed IN ('poodle', 'spaniel');")
    pprint(result)

def select_part2():
    print("select 1")
    result = execute_query("SELECT Pet.Nick, Pet_Type.Name FROM Pet, Pet_Type\
                            WHERE Pet.Pet_Type_Id = Pet_Type.Pet_Type_Id AND Pet.Nick = 'Partizan';")
    pprint(result)

    print("select 2")
    result = execute_query("SELECT Pet.Nick, Pet.Breed, Pet.Age FROM Pet, Pet_Type\
                            WHERE Pet.Pet_Type_Id = Pet_Type.Pet_Type_Id AND Pet_Type.Name = 'DOG';")
    pprint(result)

    print("select 3")
    result = execute_query("SELECT AVG(Pet.Age) FROM Pet, Pet_Type\
                            WHERE Pet.Pet_Type_Id = Pet_Type.Pet_Type_Id AND Pet_Type.Name = 'CAT';")
    pprint(result[0][0])

    print("select 4")
    result = execute_query("SELECT Order1.Time_Order, Person.Last_Name FROM Order1, Employee, Person\
                            WHERE Order1.Employee_ID = Employee.Employee_ID AND Employee.Person_ID = Person.Person_ID\
                            AND Order1.Is_Done = 0;")
    pprint(result)

    print("select 5")
    result = execute_query("SELECT Person.First_Name, Person.Last_Name, Person.phone\
                            FROM Pet, Pet_Type, Owner, Person\
                            WHERE Pet.Pet_Type_Id = Pet_Type.Pet_Type_Id AND Pet.Owner_ID = Owner.Owner_ID\
                            AND Owner.Person_Id = Person.Person_ID AND\
                            Pet_Type.Name = 'DOG';")
    pprint(result)

    print("select 6")
    result = execute_query("SELECT Pet_Type.Name, Pet.Nick\
                            FROM Pet_Type LEFT JOIN Pet\
                            ON Pet.Pet_Type_Id = Pet_Type.Pet_Type_Id\
                            ORDER BY Pet_Type.Pet_Type_ID;")
    pprint(result)

    print("select 7")
    result = execute_query("SELECT Pet.Age, Pet_Type.Name, COUNT(*)\
                            FROM Pet_Type JOIN Pet\
                            ON Pet.Pet_Type_Id = Pet_Type.Pet_Type_Id\
                            GROUP BY Pet.Age, Pet_Type.Name\
                            ORDER BY Pet.Age;")
    pprint(result)

    print("select 8")
    result = execute_query("SELECT Person.Last_Name, COUNT(*) FROM Order1, Employee, Person\
                            WHERE Order1.Employee_ID = Employee.Employee_ID AND Employee.Person_ID = Person.Person_ID\
                            AND Order1.Is_Done = 1\
                            GROUP BY Person.Person_ID\
                            HAVING COUNT(*) > 3;")
    pprint(result)


select_part1()
