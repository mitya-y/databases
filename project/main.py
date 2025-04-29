from postgre_utils import execute_query_file
from postgre_utils import execute_query
from pprint import pprint

def test_triggers():
    print()
    print("test trigger 1")
    # this must be successfull
    execute_query("DELETE FROM Account WHERE account_id = 101;")
    res = execute_query("SELECT active, value FROM Account WHERE account_id = 101;")
    pprint(res)

    # here must be error, cannot delete not empty account
    execute_query("DELETE FROM Account WHERE account_id = 102;")
    res = execute_query("SELECT active, value FROM Account WHERE account_id = 102;")
    pprint(res)

    print()
    print("test trigger 2")
    # client 3 can create kredit, he has not any yet
    execute_query("INSERT INTO Account (account_id, active, valute_id,\
                   value, client_id, account_type_id, create_date) VALUES\
                   (109, TRUE, 4, 0.0, 3, 2, '2023-05-07')")
    res = execute_query("SELECT * FROM Account WHERE account_id = 109;")
    pprint(res)

    # client 1 can not create kredit, he has other kredit already
    execute_query("INSERT INTO Account (account_id, active, valute_id,\
                   value, client_id, account_type_id, create_date) VALUES\
                   (110, TRUE, 3, 0.0, 1, 2, '2023-06-17')")
    res = execute_query("SELECT * FROM Account WHERE account_id = 110;")
    pprint(res)

    print()
    print("test trigger 3")
    # before delete client 3
    # TODO: select from ActualTable view
    res = execute_query("SELECT * FROM Account WHERE client_id = 3;")
    pprint(res)

    # client 1 can not create kredit, he has other kredit already
    execute_query("DELETE FROM Client WHERE client_id = 3;")
    res = execute_query("SELECT * FROM Account WHERE client_id = 3;")
    pprint(res)

def test_views():
    print()
    print("test view 1")
    # show all accounts of Мария Петорова
    query = "SELECT * FROM ActiveAccountsStat WHERE\
             client_name = 'Мария' AND client_surname = 'Петрова'"
    res = execute_query(query + ';')
    pprint(res)

    # delete kredit account
    execute_query(f"DELETE FROM Account WHERE account_id IN\
                    (SELECT account_id FROM ({query}) WHERE account_type = 'Кредитный');")
    res = execute_query(query + ';')
    pprint(res)

    print()
    print("test view 3")
    res = execute_query("SELECT * FROM AllTranslates;")
    pprint(res)




#==========================================================================
# test part
#==========================================================================

execute_query_file("scripts/bank/create.sql")
print("tables were created")

execute_query_file("scripts/bank/add_fk.sql")
print("fk were added")

execute_query_file("scripts/triggers.sql")
print("triggers were added")

execute_query_file("scripts/views.sql")
print("views were added")

execute_query_file("scripts/bank/fill.sql")
print("tables were filled by initial data")

print()
print('----------------------')
print('tests')

test_triggers()
test_views()

print()
print('----------------------')
print('delete')
print()


execute_query_file("scripts/bank/delete.sql")
print("tables was droped")