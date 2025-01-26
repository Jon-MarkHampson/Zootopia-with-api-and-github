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


def generate_animals_html_content(animals_data):
    """Generates the HTML content for all animals."""
    html_output = []
    for animal in animals_data:
        individual_animal_dict = {
            "Name": animal.get("name"),
            "Diet": animal.get("characteristics", {}).get("diet"),
            "Location": ", ".join(animal.get("locations", [])),
            "Type": animal.get("characteristics", {}).get("type"),
        }
        # Remove None or empty values
        individual_animal_dict = {k: v for k, v in individual_animal_dict.items() if v}
        html_output.append(concat_dict_to_html_format(individual_animal_dict))
    return "\n".join(html_output)


def process_and_save_template(template_file, placeholder, html_content, output_file):
    """
    Reads the template, replaces the placeholder with HTML content,
    and writes the result to the output file.
    """
    with open(template_file, "r", encoding="utf-8") as file:
        template = file.read()
    modified_html = template.replace(placeholder, html_content)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(modified_html)


def main():
    """Main function to generate the animals.html file."""
    # File paths
    template_file = "animals_template.html"
    data_file = "animals_data.json"
    output_file = "animals.html"

    placeholder_text_in_template = "__REPLACE_ANIMALS_INFO__"

    animals_data = load_data(data_file)
    animals_html_content = generate_animals_html_content(animals_data)
    process_and_save_template(template_file, placeholder_text_in_template, animals_html_content, output_file)


if __name__ == "__main__":
    main()
