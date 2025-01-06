from database import Database
from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()

#script for screating table
if len(argv) > 1 and argv[1] == 'setup':
    '''
        Initialize Database
        Usage: python main.py setup
    '''
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))
    #columns: id   kategoria   url
    db.create_table(
        '''
        CREATE TABLE urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            category TEXT, 
            url TEXT
        )
        '''
    )
    print("Tabela została utworzona pomyślnie.")


#adding items into db into dbeaver
if len(argv) == 4 and argv[1] == 'add':
    '''
    Adding new item into db
    python main.py add https://www.webszyk.pl
    '''
    print('Dodaje nowy adres url')
    category = argv[2]
    url = argv[3]
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)

if len(argv) == 3 and argv[1] == 'list':
    print(f'Lista linków z kategorii: {argv[2]}')
    category = argv[2]
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls',category=category)

    for link in links:
        print(link[2])

#checking variable
# print(getenv('DB_NAME'))
