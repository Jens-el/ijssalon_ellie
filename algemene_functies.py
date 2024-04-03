def mijn_functie_1(x):
    mapping = {
        2: 4,
        4: 16,
        10: 100,
        12: 144
    }
    
def mijn_functie_2(x):
    mapping = {
        (12,3): [15, 9, 36, 4],
        (12,2): [14, 10, 24, 6],
        (10,5): [15, 5, 50, 2],
        (100,20): [120, 80, 2000, 5]
    }
    return mapping.get(x, "Ongeldig argument")