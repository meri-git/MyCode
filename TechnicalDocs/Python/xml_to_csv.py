import xml.etree.ElementTree as ET
import csv

def xml_to_csv(input_file, output_file):
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create a CSV file and write header
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Get the header from the first child element
        header = [child.tag for child in root[0]]
        csvwriter.writerow(header)

        # Write each child element as a row in the CSV file
        for child in root:
            row_data = [child.find(tag).text if child.find(tag) is not None else "" for tag in header]
            csvwriter.writerow(row_data)

if __name__ == "__main__":
    input_xml_file = "input.xml"   # Replace with the path to your input XML file
    output_csv_file = "output.csv" # Replace with the desired output CSV file name

    xml_to_csv(input_xml_file, output_csv_file)
