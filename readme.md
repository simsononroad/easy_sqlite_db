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

# example:
```
init_db("database.db")
create_table("database.db", "tabla", ["elso_oszlop", "második_oszlop"])
add_element("database.db" ,"tabla", ["elso_oszlop", "második_oszlop"], ["content", "masodik"])
```
<img src="code_snap.PNG">