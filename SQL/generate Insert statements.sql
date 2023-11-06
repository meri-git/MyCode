-- Replace your_database and your_table with the actual database and table names
SELECT 
  'INSERT INTO your_table (' ||
  LISTAGG("column_name", ', ') WITHIN GROUP (ORDER BY ordinal_position) ||
  ') VALUES (' ||
  LISTAGG(
    CASE
      WHEN data_type IN ('NUMBER', 'FLOAT', 'DOUBLE', 'INT', 'BIGINT', 'BOOLEAN') THEN column_name
      ELSE 'CONVERT(VARIANT, ' || column_name || ')'
    END, 
    ', '
  ) WITHIN GROUP (ORDER BY ordinal_position) ||
  ');'
FROM information_schema.columns
WHERE table_schema = 'your_database' -- Replace with your actual database name
  AND table_name = 'your_table';    -- Replace with your actual table name
