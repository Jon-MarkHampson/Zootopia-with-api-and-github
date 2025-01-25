import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

animals_data = load_data('animals_data.json')

output = ""
for animal in animals_data:
    name = animal.get('name')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet')
    locations = animal.get('locations')
    animal_type = characteristics.get('type')

    if name:
        output += f"Name: {name}\n"
    if diet:
        output += f"Diet: {diet}\n"
    if locations:
        output += f"Location: {locations[0]}\n"
    if animal_type:
        output += f"Type: {animal_type}\n"
    output += "\n"

modified_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(modified_html_content)
