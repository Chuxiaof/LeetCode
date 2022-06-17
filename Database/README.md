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
    - interger: INTEGER = INT, "signed" by default eg., INTEGER(8)
    - fixed-point: DECIMAL = NUMERIC, eg., DECIMAL(5, 3) 10.768
    - floating-point: FLOAT, eg., FLOAT(7, 2) 10374.07

- Date and Time
    - DATE: YYYY-MM-DD e.g., 2018-07-25
    - DATETIME: YYYY-MM-DD HH:MM:SS[.fraction], 0-23:59:59.999999, e.g., 2018-07-25 09:30:00
    - TIMESTAMP: number of seconds after 1st Jan 1970 00:00:00

### Creating a table
-   ```
    CREATE TABLE table_name 
    (
        column_1 data_type constraints,
        column_2 data_type constraints,
        ...
        column_n data_type constraints
    );
    ```
    - compulsory requirement: sdd at least one columm


### Delete a table

-   ```
    DROP TABLE table_name;
    ```

### MySQL Constraints

- PRIMARY KEY Constraints
    ```
    PRIMARY KEY (column_name)
    ```

- FOREIGN KEY Constraints
    ```
    FOREIGN KEY (column_name1) REFERENCES child_table_name(column_name2) ON DELETE CASCADE
    ```
    - parent table = referenced table
    - child table = referencing table
    - CASCADE means want a certain phenomenon toaffect dependent objects together at the same time
    - ON DELETE CASCADE means if a specific value from the parent table's primary key has been deleted, all the records from the child table referring to this value will be removed as well
    
    - Add FOREIGN KEY Constraints
        ```
        ALTER TABLE table_name
        ADD FOREIGN KEY (column_name1) REFERENCES customers(column_name2) ON DELETE CASCADE;
        ```

    - Remove FOREIGN KEY Constraints
        ```
        ALTER TABLE table_name
        DROP FOREIGN KEY foreign_key_name;
        ```
    

    - UNIQUE KEY Constraints
        ```
        UNIQUE KEY (column_name)
        ```

        - Add FOREIGN KEY Constraints
            ```
            ALTER TABLE table_name
            ADD UNIQUE KEY (column_name1);
            ```

        - Remove UNIQUE KEY Constraints
            ```
            ALTER TABLE table_name
            DROP INDEX unique_key_field;
            ```

    - DEFAULT Constraints
        - e.g,
            ```
            col_name INT DEFAULT 0
            ```
        
        - Add DEFAULT Constraints
            ```
            ALTER TABLE table_name
            CHANGE COLUMN Col_name1 Col_name2 INT DEFAULT 0;
            ```

        - Remove DEFAULT Constraints
            ```
            ALTER TABLE table_name
            ALTER COLUMN Col_name DROP DEFAULT;
            ```


    - NOT NULL Constraints
        - e.g,
        ```
        col_name INT NUT NULL
        ```
        - Add DEFAULT Constraints
            ```
            ALTER TABLE table_name
            CHANGE COLUMN Col_name1 Col_name2 VARCHAR(255) NOT NULL;
            ```

        - Remove DEFAULT Constraints
            ```
            ALTER TABLE table_name
            MODIFY Col_name VARCHAR(255) NULL;
            ```

        - MODIFY COLUMN This command does everything CHANGE COLUMN can, but without renaming the column.