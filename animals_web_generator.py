import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def concat_dict_to_html_format(animal_dict):
    """Creates an HTML list item from a dictionary."""
    lines = ["<li class='cards-item'><br/>"]
    lines.extend([f"{key}: {value}<br/>" for key, value in animal_dict.items()])
    lines.append("</li>")
    return "\n".join(lines)


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

animals_data = load_data('animals_data.json')

animal_html_output = ""
for animal in animals_data:
    name = animal.get('name')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet')
    locations = animal.get('locations')
    animal_type = characteristics.get('type')

    individual_animal_dict = {}

    if name:
        individual_animal_dict["Name"] = name
    if diet:
        individual_animal_dict["Diet"] = diet
    if locations:
        individual_animal_dict["Location"] = locations[0]
    if animal_type:
        individual_animal_dict["Type"] = animal_type

    animal_html_output += concat_dict_to_html_format(individual_animal_dict)

modified_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animal_html_output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(modified_html_content)
