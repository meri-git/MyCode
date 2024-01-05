import re

def format_table_view_ddl(input_file, output_file):
    with open(input_file, 'r') as infile:
        sql_content = infile.read()

        # Using regular expressions to match CREATE TABLE statements
        table_ddl_pattern = re.compile(r'CREATE\s+(OR\s+REPLACE\s+)?TABLE (\S+) \((.*?)\);', re.DOTALL)

        def format_columns(match):
            replace = match.group(1) if match.group(1) else ''
            table_name = match.group(2)
            columns = match.group(3).strip()
            formatted_columns = split_columns(columns)
            return f'CREATE {replace}TABLE {table_name}\n({formatted_columns}\n);'

        def split_columns(columns):
            split_cols = []
            current_col = ''
            within_parentheses = False

            for char in columns:
                if char == ',' and not within_parentheses:
                    split_cols.append(current_col.strip())
                    current_col = ''
                else:
                    current_col += char
                    if char == '(':
                        within_parentheses = True
                    elif char == ')':
                        within_parentheses = False

            if current_col.strip():
                split_cols.append(current_col.strip())

            return '\n'.join(split_cols)

        # Apply formatting to each CREATE TABLE statement in the file
        formatted_sql = table_ddl_pattern.sub(format_columns, sql_content)

        # Write formatted SQL to output file
        with open(output_file, 'w') as outfile:
            outfile.write(formatted_sql)

# Replace 'input.sql' and 'output.sql' with your file names
input_file = 'input.sql'
output_file = 'output.sql'

format_table_view_ddl(input_file, output_file)
