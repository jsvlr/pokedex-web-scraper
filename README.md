# Pokémon Scraper and Database Creator

This project is a Python script that scrapes Pokémon data from the [Pokémon Database](https://pokemondb.net/pokedex/all) and stores it in a SQLite database.

## Features

- Scrapes Pokémon data including their number, name, type, and other attributes from the Pokémon Database website.
- Stores the scraped data in a SQLite database.
- Creates a table in the SQLite database if it does not already exist.
- Performs a bulk insert operation to populate the table with the scraped data.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `sqlite3` (comes with Python standard library)

You can install the required libraries using pip:

```sh
pip install requests beautifulsoup4
```
