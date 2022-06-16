## database
### Data Definition Language (DDL): creation of data
    - CREATE
    - ALTER
    - DROP
    - RENAME
    - TRUNCATE

### Data Manipulate Language (DDL): manipulation of data
    - SELECT FROM
    - INSERT INTO VALUES
    - UPDATE SET WHERE
    - DELETE FROM WHERE

### Data Control Language (DCL): assignment or removal of permissions to use this data
    - GRANT TO 
    - REVOKE FROM

### Transaction Control Language (TCL): saving andrestoring changes to a database
    - COMMIT
    - ROLLBACK


### Creating a database
-   ```
    CREATE DATABASE [IF NOT EXISTS] database_name;
    ```
    - [] optional. can be typed or ommited
    - no diff between upper/lowercase
    - no diff between " ", ' ', or no quotes
    - ; can be omitted but had better not to
    - execute = Ctrl + Shift + Enter

-   ```
    USE sales;
    ```
    
### Data Types 
- (MySQL: 3 main data types: string, numeric, and date and time.)
- String Data Types:
    - character: CHAR, eg., CHAR(5)
    - variable character: VARCHAR, eg., VARCHAR(5)
    - enumerate: ENUM
- Numeric
- Date and Time

### Creating a table
-   ```
    DREATE TABLE table_name 
    (
        column_1 data_type constraints,
        column_2 data_type constraints,
        ...
        column_n data_type constraints
    );
    ```
    - compulsory requirement: sdd at least one columm


