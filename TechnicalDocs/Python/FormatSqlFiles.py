def format_table_view_ddl(input_file, output_file):
    with open(input_file, 'r') as infile:
        sql_content = infile.read()

        # Using regular expressions to match CREATE TABLE statements
        table_ddl_pattern = re.compile(r'CREATE\s+(OR\s+REPLACE\s+)?TABLE (\S+) \((.*?)\);', re.DOTALL)

        def format_columns(match):
            replace = match.group(1) if match.group(1) else ''
            table_name = match.group(2)
            columns = match.group(3).strip().split(',')
            formatted_columns = '\n'.join(column.strip() for column in columns)
            return f'CREATE {replace}TABLE {table_name}\n({formatted_columns}\n);'

        # Apply formatting to each CREATE TABLE statement in the file
        formatted_sql = table_ddl_pattern.sub(format_columns, sql_content)

        # Write formatted SQL to output file
        with open(output_file, 'w') as outfile:
            outfile.write(formatted_sql)

# Replace 'input.sql' and 'output.sql' with your file names
input_file = 'input.sql'
output_file = 'output.sql'

format_table_view_ddl(input_file, output_file)
