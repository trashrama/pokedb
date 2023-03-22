
lista = [
    (25, 26, 'Thunder Stone'),
    (30, 31, 'Moon Stone'),
    (33, 34, 'Moon Stone'),
    (35, 36, 'Moon Stone'),
    (37, 38, 'Fire Stone'),
    (39, 40, 'Moon Stone'),
    (044, 045, 'Leaf Stone'),
    (058, 059, 'Fire Stone'),
    (061, 062, 'Water Stone'),
    (070, 071, 'Leaf Stone'),
    (090, 091, 'Water Stone'),
    (0102, 0103, 'Leaf Stone'),
    (0120, 0121, 'Water Stone'),
    (0133, 0134, 'Water Stone'),
    (0133, 0135, 'Thunder Stone'),
    (0133, 0136, 'Fire Stone'),
    (0191, 0192, 'Sun Stone'),
    (0271, 0272, 'Water Stone'),
    (0274, 0275, 'Leaf Stone'),
    (0300, 0301, 'Moon Stone')
]

for id1, id2, pedra in lista:
    print(f"({id1}, {id2}, 'STONE', '{pedra}'),")
