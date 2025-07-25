# Cocktail Recommender Project

This project is a cocktail recommendation system that uses vector embeddings to find cocktails similar to a user's query.

## Project Structure

```
.
├── .env              # Environment variables (database credentials, API keys)
├── .gitignore        # Files to be ignored by Git
├── conected_psql.py  # Database connection and setup script
├── data_prosecced.py # Script to process and store cocktail data
├── test.py           # Script to test cocktail recommendations
├── requirements.txt  # Dependencies for the project
├── README.md         # Project documentation
└── data/
    └── final_cocktails.csv # Cocktail dataset
```

## Features

- Loads cocktail data from a CSV file.
- Generates vector embeddings for each cocktail using the Together AI API.
- Stores cocktail data and embeddings in a PostgreSQL database with pgvector.
- Provides a recommendation script to find similar cocktails based on a text query.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Create a `.env` file:**
    Copy the `.env.example` to `.env` and fill in your database credentials and Together AI API key.

3.  **Set up the database:**
    Run the `conected_psql.py` script to create the necessary tables and extensions.
    ```bash
    python conected_psql.py
    ```

4.  **Process and store data:**
    Run the `data_prosecced.py` script to load, process, and store the cocktail data with embeddings into the database.
    ```bash
    python data_prosecced.py
    ```

## Usage

To get cocktail recommendations, run the `test.py` script:
```bash
python test.py
