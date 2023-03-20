import requests
from bs4 import BeautifulSoup

# codigo pra pegar os lugares restantes

lugares = [(0, 'National Park'),
           (1, 'Mt. Moon'),
           (2, 'Union Cave'),
           (3, 'Mt. Mortar'),
           (4, 'Route 12'),
           (5, 'Route 15'),
           (6, 'Pewter City'),
           (7, 'Pallet Town'),
           (8, 'Underground Path 5-6'),
           (9, 'Slowpoke Well'),
           (10, 'Route 23'),
           (11, 'Cerulean City'),
           (12, 'Route 2'),
           (13, 'Celadon City'),
           (14, 'Route 24'),
           (15, 'Viridian City'),
           (16, 'Dark Cave'),
           (17, 'Great Marsh'),
           (18, 'Mt. Silver'),
           (19, 'Power Plant'),
           (20, 'Route 4'),
           (21, '210'),
           (22, 'Viridian Forest'),
           (23, 'Tohjo Falls'),
           (24, 'Oreburgh City'),
           (25, 'Route 209'),
           (26, 'Vermilion City'),
           (27, 'Route 14'),
           (28, 'Cinnabar Island'),
           (29, 'Victory Road'),
           (30, 'Pokémon Tower'),
           (31, 'Route 6'),
           (32, 'Ice Path'),
           (33, 'Route 20'),
           (34, 'Route 18'),
           (35, 'Route 1'),
           (36, 'Whirl Islands'),
           (37, 'Route 22'),
           (38, 'Route 11'),
           (39, 'Safari Zone'),
           (40, 'Route 8'),
           (41, 'Seafoam Islands'),
           (42, 'Route 19'),
           (43, 'Diglett''s Cave'),
           (44, 'Pokémon Mansion'),
           (45, 'Rock Tunnel'),
           (46, 'Route 7'),
           (47, 'Route 9'),
           (48, 'Route 10'),
           (49, 'Route 3'),
           (50, 'Route 17'),
           (51, 'Cerulean Cave'),
           (52, 'Fuchsia City'),
           (53, 'Route 21'),
           (54, 'Route 16'),
           (55, 'Route 25'),
           (56, 'Route 28'),
           (57, 'Route 13'),
           (58, 'Route 5'),
           ]

page = requests.get(
    "https://bulbapedia.bulbagarden.net/wiki/Category:Red,_Blue_and_Yellow_locations")
soup = BeautifulSoup(page.content, 'html.parser')
tabela = soup.find('div', {'class': 'mw-content-ltr'})

items = tabela.find_all('a')
i = 59
for item in items:
    tem = False
    item = item.text
    item = item.replace("'", "''")

    if not ("Kanto" in item or 'Route' in item or 'Underground' in item or 'Victory' in item or 'Yellow' in item or 'Red' in item or 'Diglet' in item):
        for indice, lugar in lugares:
            if lugar == item:
                tem = True
                break
        if not (tem):
            print(f"({i}, '{item}'),")
            i = i+1
