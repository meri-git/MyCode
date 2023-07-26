import xml.etree.ElementTree as ET

def xml_to_delimited(input_file, output_file, delimiter='\t'):
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create a delimited file and write data
    with open(output_file, 'w') as delimited_file:
        # Write the header row based on the first child element
        header = [child.tag for child in root[0]]
        delimited_file.write(delimiter.join(header) + '\n')

        # Write each child element as a row in the delimited file
        for child in root:
            row_data = [child.find(tag).text if child.find(tag) is not None else "" for tag in header]
            delimited_file.write(delimiter.join(row_data) + '\n')

if __name__ == "__main__":
    input_xml_file = "input.xml"   # Replace with the path to your input XML file
    output_delimited_file = "output.txt" # Replace with the desired output delimited file name

    xml_to_delimited(input_xml_file, output_delimited_file, delimiter='\t')
