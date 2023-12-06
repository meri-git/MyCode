SELECT a.column_name AS column_in_your_table, b.column_name AS column_in_related_table
FROM all_cons_columns a
JOIN all_constraints c ON a.owner = c.owner AND a.table_name = c.table_name AND a.constraint_name = c.constraint_name
JOIN all_constraints r ON c.r_owner = r.owner AND c.r_constraint_name = r.constraint_name
JOIN all_cons_columns b ON r.owner = b.owner AND r.table_name = b.table_name AND r.constraint_name = b.constraint_name
WHERE a.owner = 'YOUR_SCHEMA_NAME' AND a.table_name = 'YOUR_TABLE_NAME' AND c.constraint_type = 'R';