def format_table_view_ddl(input_file, output_file):
    with open(input_file, 'r') as infile:
        # Read the content of the input file
        input_content = infile.read()

        # Splitting by space and removing unnecessary characters
        tokens = input_content.replace('(', ';\n(').replace(')', '\n)').split()

        formatted_output = ""
        for token in tokens:
            if token == '(':
                formatted_output = formatted_output.rstrip() + '\n' + token
            elif token == ',':
                formatted_output = formatted_output.rstrip() + '\n' + token + ' '
            else:
                formatted_output += ' ' + token

    with open(output_file, 'w') as outfile:
        outfile.write(formatted_output)

# Replace 'input.sql' and 'output.sql' with your file names
input_file = 'input.sql'
output_file = 'output.sql'

format_table_view_ddl(input_file, output_file)
