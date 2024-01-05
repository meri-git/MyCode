import sqlparse

def format_ddls_in_sql_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        sql_content = infile.read()

        # Split SQL content into individual statements
        statements = sqlparse.split(sql_content)

        formatted_statements = []
        for statement in statements:
            # Parse and format each individual statement
            parsed = sqlparse.format(statement, reindent=True, keyword_case='upper')
            formatted_statements.append(parsed)

        formatted_sql = '\n'.join(formatted_statements)

        # Write formatted SQL to output file
        with open(output_file, 'w') as outfile:
            outfile.write(formatted_sql)

# Replace 'input.sql' and 'output.sql' with your file names
input_file = 'input.sql'
output_file = 'output.sql'

format_ddls_in_sql_file(input_file, output_file)
