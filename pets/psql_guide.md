Чтобы посмотреть данные в таблице PostgreSQL, выполните следующие шаги:

---

### **1. Подключитесь к базе данных**
```bash
sudo -u postgres psql -d имя_базы  # Замените имя_базы на ваше (например, pet-db)
```

---

### **2. Посмотрите список таблиц**
```sql
\dt
```
Пример вывода:
```
          List of relations
 Schema |   Name    | Type  |  Owner   
--------+-----------+-------+----------
 public | users     | table | postgres
 public | products  | table | postgres
```

---

### **3. Посмотрите данные внутри таблицы**
```sql
SELECT * FROM имя_таблицы;  # Например, SELECT * FROM users;
```
Пример вывода:
```
 id |  name  | age 
----+--------+-----
 1  | Alice  | 30
 2  | Bob    | 25
```

---

### **4. Просмотр структуры таблицы (столбцы и типы данных)**
```sql
\d имя_таблицы
```
Пример вывода:
```
       Table "public.users"
 Column |  Type   | Collation | Nullable 
--------+---------+-----------+----------
 id     | integer |           | not null 
 name   | text    |           | not null 
 age    | integer |           | 
```

---

### **5. Примеры фильтрации данных**
#### Показать первые 10 строк:
```sql
SELECT * FROM users LIMIT 10;
```

#### Выбрать конкретные столбцы:
```sql
SELECT name, age FROM users;
```

#### Фильтрация по условию:
```sql
SELECT * FROM users WHERE age > 25;
```

---

### **6. Если вы не знаете имя базы данных**
#### Посмотрите список всех баз:
```sql
\l
```

#### Переключитесь на нужную базу:
```sql
\c имя_базы
```

---

### **7. Выход из psql**
```sql
\q
```

---

### **Важно!**
- Если таблица пустая, `SELECT *` не выведет ничего.
- Для больших таблиц используйте `LIMIT`, чтобы не перегружать консоль.
- Если нет прав на чтение таблицы, запросите их у администратора.

---

Теперь вы можете легко исследовать данные в своих таблицах! 🗃️

#### Про дейттайм

Ошибка возникает, потому что в PostgreSQL нет типа DATETIME. Вместо него используйте TIMESTAMP или TIMESTAMPTZ (с часовым поясом). Также функция GETDATE() не существует в PostgreSQL — используйте NOW() или CURRENT_TIMESTAMP.

#### Исполнение скриптов:
```sql
sudo -u postgres psql -d mydb -f /path/to/script.sql
```

если изнутри консоли:
```bash
sudo -u postgres psql -d mydb
```
```sql
\i /path/to/script.sql
```

