# Install
1. Write to the terminal: `https://github.com/simsononroad/easy_db__Python_libary.git`

2. Create a .py file
3. import: `from easy_db.init import *`

# usage
- `init_db(database_name)` 
    - -> database_name: `str`
- `create_table(database_name, table_name, columns)`
    - -> database_name: `str`
    - -> table_name: `str`
    - -> columns: `list`

- `add_element(database_name, table_name, columns, content)`
    - -> database_name: `str`
    - -> table_name: `str`
    - -> columns: `list`
    - -> content: `list`
- `select_item(database_name, table_name, columns)`, return -> Items
    - -> database_name: `str`
    - -> table_name: `str`
    - -> columns: `str`

# example:
```
init_db("database.db")
create_table("database.db", "tabla", ["elso_oszlop", "második_oszlop"])
add_element("database.db" ,"tabla", ["elso_oszlop", "második_oszlop"], ["content", "masodik"])
output = select_item("database.db", "tabla", "elso_oszlop)

```
<img src="code_snap.PNG">

- or

```
init_db(db_name="database.db")
create_table(db_name="database.db", table_name="tabla", column_name=["elso_oszlop", "második_oszlop"])
add_element(db_name="database.db", table_name="tabla", column_name=["elso_oszlop", "második_oszlop"], contents=["content", "masodik"])
output = select_item(table_name="tabla", db_name="database.db", column_name="elso_oszlop")
```
<img src="code_snap2.PNG">