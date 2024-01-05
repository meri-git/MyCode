import sqlparse

def format_columns_separate_rows(input_file, output_file):
    with open(input_file, 'r') as infile:
        sql_content = infile.read()

        # Split SQL content into individual statements
        statements = sqlparse.split(sql_content)

        formatted_statements = []
        for statement in statements:
            parsed = sqlparse.parse(statement)
            for stmt in parsed:
                # Filter out non-DDL statements (e.g., comments)
                if stmt.get_type() != 'CREATE':
                    continue
                
                # Extract and format column names in separate rows
                for token in stmt.tokens:
                    if isinstance(token, sqlparse.sql.IdentifierList):
                        for identifier in token.get_identifiers():
                            formatted_statements.append(identifier.normalized)
                    elif token.ttype is sqlparse.tokens.Keyword and token.value.upper() == 'CREATE':
                        formatted_statements.append(token.value.upper())
                    elif token.ttype is sqlparse.tokens.Keyword and token.value.upper() == 'TABLE':
                        formatted_statements.append(token.value.upper())
                    elif isinstance(token, sqlparse.sql.Parenthesis):
                        formatted_statements.append(token.value.strip())
                    else:
                        continue
                formatted_statements.append('\n')  # Separate columns by a newline

        formatted_sql = '\n'.join(formatted_statements)

        # Write formatted SQL to output file
        with open(output_file, 'w') as outfile:
            outfile.write(formatted_sql)

# Replace 'input.sql' and 'output.sql' with your file names
input_file = 'input.sql'
output_file = 'output.sql'

format_columns_separate_rows(input_file, output_file)
