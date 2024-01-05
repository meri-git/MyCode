import sqlparse

def format_ddls_with_columns_on_new_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        sql_content = infile.read()

        # Split SQL content into individual statements
        statements = sqlparse.split(sql_content)

        formatted_statements = []
        for statement in statements:
            # Parse the statement
            parsed = sqlparse.parse(statement)

            # Iterate over tokens in each statement
            formatted_statement = ""
            for token in parsed[0].tokens:
                if token.ttype in (sqlparse.tokens.Keyword, sqlparse.tokens.Name):
                    formatted_statement += '\n' + token.value
                else:
                    formatted_statement += ' ' + token.value

            formatted_statements.append(formatted_statement.strip())

        formatted_sql = '\n'.join(formatted_statements)

        # Write formatted SQL to output file
        with open(output_file, 'w') as outfile:
            outfile.write(formatted_sql)

# Replace 'input.sql' and 'output.sql' with your file names
input_file = 'input.sql'
output_file = 'output.sql'

format_ddls_with_columns_on_new_lines(input_file, output_file)
