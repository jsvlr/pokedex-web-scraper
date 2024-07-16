import requests, re, sqlite3
from bs4 import BeautifulSoup

def main():

    URL = 'https://pokemondb.net/pokedex/all'

    get_pokemons = requests.get(URL)
    scraper = BeautifulSoup(get_pokemons.text, 'html.parser')


    # This line is locating the table that contains the data for all the Pokemon on the webpage.
    pokemon_table = scraper.find('table', attrs={'id':'pokedex'})

    # The lines `pattern = r"[.\s]"` and `replacement = ''` are setting up a regular expression pattern
    # and replacement string for later use in the code.
    pattern = r"[.\s]"
    replacement = ''

    # The code snippet you provided is responsible for extracting the headers and rows of data from the
    # HTML table containing Pokemon information on the webpage
    headers = [re.sub(pattern, replacement, h.text.strip()) for h in pokemon_table.find('thead').find_all('th')]
    headers[0] = 'No'

    # `rows = pokemon_table.find('tbody').find_all('tr')` is finding all the table row elements
    # (`<tr>`) within the `<tbody>` section of the HTML table identified by the variable
    # `pokemon_table`.
    rows = pokemon_table.find('tbody').find_all('tr')

    pokemon_container = []

    def to_str(col):
        if len(col.find_all('a')) > 1:
            return ','.join([_.text.strip() for _ in col.find_all('a')])
        return col.text.strip()

    # This block of code is iterating over each row (`<tr>`) in the table body of the HTML table that
    # contains Pokemon information. For each row, it finds all the table data cells (`<td>`) within
    # that row.
    for p in rows:
        cols = p.find_all('td')
        pokemon_container.append([to_str(i) for i in cols])

    # create connection to pokemon db
    con = sqlite3.connect('pokemon.db')
    cursor = con.cursor()

    # is creating a SQL query to create a table in the SQLite database if it does not already exist.
    cursor.execute(f"CREATE TABLE IF NOT EXISTS pokemon_tbl(" + ','.join(headers) + ")")


    # performed a bulk insert operation
    # into the SQLite database table named `pokemon_tbl`.
    cursor.executemany(f"INSERT INTO pokemon_tbl({','.join(headers)}) VALUES ({','.join(['?'] * len(headers))})",pokemon_container)
    
    # commit all transaction
    con.commit()
    con.close()

if __name__ == "__main__":
    main()