# Animal Data Website Generator

This Python project generates a static HTML website to display data about animals, including their characteristics and taxonomy, fetched from an API. The user can input an animal name and filter the results based on the animal's skin type. The website is dynamically created based on the fetched data, with fallback handling for cases where the animal doesn't exist.

---

## Features

- Fetches animal data from [API Ninjas](https://api-ninjas.com/) using an API key stored securely in a `.env` file.
- Dynamically generates an HTML page (`animals.html`) with animal details such as:
  - Name
  - Diet
  - Location
  - Type
  - Most distinctive feature
  - Scientific name
  - Biggest threat
- Allows users to filter animals by skin type.
- Displays an error message in the generated HTML if the requested animal does not exist.

---

## How It Works

1. The user is prompted to input an animal name.
2. The program fetches data for the animal from the API.
3. If data is found:
   - The available skin types are displayed.
   - The user selects a skin type to filter the data.
   - The filtered data is formatted and inserted into an HTML template.
4. If the animal does not exist, an error message is displayed in the HTML.
5. The final HTML file (`animals.html`) is generated and saved.

---

## Project Structure

. ├── data_fetcher.py # Handles API data fetching ├── animals_web_generator.py # Generates the HTML content and handles user input ├── animals_template.html # Template file for the generated HTML ├── .env # Environment variables file (contains the API key) ├── animals.html # Generated output file └── requirements.txt # Contains project dependencies

---

## Setup Instructions

### 1. Install Dependencies

Ensure you have Python installed. Install the necessary dependencies listed in `requirements.txt`:


pip install -r requirements.txt

### 2. Set Up the .env File

Create a .env file in the project directory and add your API key:

### 3. Run the Program

Execute the animals_web_generator.py script:


python animals_web_generator.py

### 4. View the Generated Website

After the program runs successfully, open the animals.html file in your browser to view the generated content.

## Usage Example

User Input:

Please enter an animal to collect data about: Fox
Output in animals.html:

<li class="cards__item">
    <div class="card__title">Fox</div>
    <ul class="card__details">
        <li class="card__detail-item" data-label="Diet:">Carnivore</li>
        <li class="card__detail-item" data-label="Location:">North America</li>
        <li class="card__detail-item" data-label="Type:">Mammal</li>
        <li class="card__detail-item" data-label="Scientific Name:">Vulpes vulpes</li>
    </ul>
</li>

## Error Handling

If the user inputs an invalid animal name (e.g., goadohjasgfas), the program generates an error message in the HTML:


<h2>The animal 'goadohjasgfas' doesn't exist.</h2>

## Environment Variables

This project uses python-dotenv to load sensitive information, such as the API key, from a .env file. This enhances security by keeping such data out of the codebase.

## Dependencies

The project dependencies are listed in the requirements.txt file. Install them using:

pip install -r requirements.txt


## Contributing

Feel free to fork the repository and submit pull requests with improvements or new features!