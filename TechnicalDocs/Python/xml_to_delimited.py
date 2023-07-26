import xml.etree.ElementTree as ET
import csv

def flatten_xml_child_nodes(element):
    # Flatten the XML structure of a given element and its children into a single string
    flattened_data = []
    for child in element:
        flattened_data.append(ET.tostring(child, encoding='unicode'))
    return '\n'.join(flattened_data)

def xml_to_delimited(input_file, output_file, delimiter='\t'):
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create a delimited file and write data
    with open(output_file, 'w', newline='') as delimited_file:
        csvwriter = csv.writer(delimited_file, delimiter=delimiter)

        # Write each child node as a separate row in the delimited file
        for child in root:
            row_data = [flatten_xml_child_nodes(child)]
            csvwriter.writerow(row_data)

if __name__ == "__main__":
    input_xml_file = "input.xml"   # Replace with the path to your input XML file
    output_delimited_file = "output.txt" # Replace with the desired output delimited file name

    xml_to_delimited(input_xml_file, output_delimited_file, delimiter='\t')
