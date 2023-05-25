CREATE OR REPLACE PROCEDURE InsertTableDDLsIntoTable(schema_name STRING, target_table STRING)
RETURNS VARCHAR
LANGUAGE SQL
AS
$$
  -- Declare variables
  DECLARE
    table_name STRING;
    ddl_statement STRING;
  
  -- Cursor to fetch table names
  DECLARE cursor_tables CURSOR FOR
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = schema_name;
  
  -- Loop through table names
  BEGIN
    FOR table_rec IN cursor_tables DO
      table_name := table_rec.TABLE_NAME;
      
      -- Generate DDL statement
      ddl_statement := (SELECT GET_DDL('TABLE', schema_name || '.' || table_name));
      
      -- Insert DDL statement into target table
      EXECUTE IMMEDIATE 'INSERT INTO ' || target_table || '(table_name, ddl_statement) VALUES (:1, :2)'
      USING table_name, ddl_statement;
      
    END FOR;
  END;
  
  -- Return a success message
  RETURN 'DDL statements inserted into ' || target_table;
$$;

-- Call the procedure
CALL InsertTableDDLsIntoTable('your_schema_name', 'your_target_table_name');
