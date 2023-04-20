import snowflake.connector

# set up connection parameters
user = '<your_username>'
password = '<your_password>'
account = '<your_account_name>'
warehouse = '<your_warehouse_name>'
database = '<your_database_name>'
schema = '<your_schema_name>'

# create connection object
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)

# define SQL statements for schema evolution
create_table_sql = '''
    CREATE TABLE users (
        id INT,
        name VARCHAR(50),
        email VARCHAR(100)
    )
'''

add_column_sql = '''
    ALTER TABLE users ADD COLUMN age INT
'''

# execute schema evolution statements
try:
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    cursor.execute(add_column_sql)
    conn.commit()
    print('Schema evolution completed successfully!')
except Exception as e:
    print(f'Error executing schema evolution: {e}')

# close connection
conn.close()
------------------------------------------------------------------------------

import snowflake.connector

def create_or_update_table():
    conn = snowflake.connector.connect(
        user='<username>',
        password='<password>',
        account='<account_name>',
        warehouse='<warehouse_name>',
        database='<database_name>',
        schema='<schema_name>',
    )

    try:
        cursor = conn.cursor()

        # Check if table exists in schema
        cursor.execute(f"SHOW TABLES IN {schema}")
        tables = [table[0].lower() for table in cursor.fetchall()]
        if 'users' not in tables:
            # Create table if it does not exist
            cursor.execute('''
                CREATE TABLE users (
                    id INT,
                    name VARCHAR(50),
                    email VARCHAR(100)
                )
            ''')
        else:
            # Add column if it does not exist
            cursor.execute('''
                ALTER TABLE users ADD COLUMN age INT
            ''')

        # Commit changes
        conn.commit()
        print('Schema evolution completed successfully!')
    except Exception as e:
        print(f'Error executing schema evolution: {e}')
    finally:
        conn.close()

# Create the stored procedure
conn = snowflake.connector.connect(
    user='<username>',
    password='<password>',
    account='<account_name>',
    warehouse='<warehouse_name>',
    database='<database_name>',
    schema='<schema_name>',
)

try:
    cursor = conn.cursor()

    # Create or replace the stored procedure
    cursor.execute('''
        CREATE OR REPLACE PROCEDURE create_or_update_users_table()
        RETURNS VARCHAR
        LANGUAGE PYTHON
        EXECUTE AS OWNER
        AS
        '''
        + create_or_update_table.__code__.co_code.hex() +
        '''
        ;
    ''')
    conn.commit()
    print('Stored procedure created successfully!')
except Exception as e:
    print(f'Error creating stored procedure: {e}')
finally:
    conn.close()
