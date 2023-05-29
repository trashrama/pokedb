lista_lugares = ['National Park', 'Mt. Moon', 'Union Cave', 'Mt. Mortar', 'Route 12', 'Route 15', 'Pewter City', 'Pallet Town', 'Underground Path 5-6', 'Slowpoke Well', 'Route 23', 'Cerulean City', 'Route 2', 'Celadon City', 'Route 24', 'Viridian City', 'Dark Cave', 'Great Marsh', 'Mt. Silver', 'Power Plant', 'Route 4', '210', 'Viridian Forest', 'Tohjo Falls', 'Oreburgh City', 'Route 209', 'Vermilion City', 'Route 14',
                 'Cinnabar Island', 'Victory Road', 'Pokémon Tower', 'Route 6', 'Ice Path', 'Route 20', 'Route 18', 'Route 1', 'Whirl Islands', 'Route 22', 'Route 11', 'Safari Zone', 'Route 8', 'Seafoam Islands', 'Route 19', "Diglett''s Cave", 'Pokémon Mansion', 'Rock Tunnel', 'Route 7', 'Route 9', 'Route 10', 'Route 3', 'Route 17', 'Cerulean Cave', 'Fuchsia City', 'Route 21', 'Route 16', 'Route 25', 'Route 28', 'Route 13', 'Route 5']


f = open("lugares.txt", 'a')
for i in range(len(lista_lugares)):
    f.writelines(f"('{lista_lugares[i]}'),\n")
f.close()
