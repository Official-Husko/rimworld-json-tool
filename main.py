import xmltodict
import json
import os

if not os.path.exists("input"):
    os.makedirs("input")
if not os.path.exists("output"):
    os.makedirs("output")

def convert_to_xml(input_path, output_xml_path):
    with open(input_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # Convert JSON to XML
    xml_data = xmltodict.unparse(json_data, pretty=True)

    # Save the XML to a new file
    filename = os.path.basename(file).replace(".json", ".xml")
    with open(f"output/{filename}", "w", encoding="utf-8") as f:
        f.write(xml_data)

def convert_to_json(input_path, output_json_path):
    with open(input_path, "r", encoding="utf-8") as f:
        xml_data = f.read()

    # Parse XML to dictionary
    xml_dict = xmltodict.parse(xml_data)

    # Save the dictionary as JSON to a new file
    filename = os.path.basename(file).replace(".xml", ".json")
    with open(f"output/{filename}", "w", encoding="utf-8") as f:
        json.dump(xml_dict, f, indent=2)

# Use the provided file paths
output_xml_file = r"output\output.xml"
output_json_file = r"output\output.json"

found_files = os.listdir("input")

valid_files = []

for file in found_files:
    _, file_extension = os.path.splitext(file)
    if file_extension.lower() in [".json", ".xml"]:
        valid_files.append(os.path.join("input", file))

for file in valid_files:
    try:
        _, file_extension = os.path.splitext(file)
        if file_extension.lower() == ".json":
            convert_to_xml(file, output_xml_file)
        elif file_extension.lower() == ".xml":
            convert_to_json(file, output_json_file)

        file = os.path.basename(file)
        print(f"Processed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
