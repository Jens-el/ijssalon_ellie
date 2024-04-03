def mijn_functie_2(x):
    mapping = {
        (12,3): [15, 9, 36, 4],
        (12,2): [14, 10, 24, 6],
        (10,5): [15, 5, 50, 2],
        (100,20): [120, 80, 2000, 5]
    }
    return mapping.get(x, "Ongeldig argument")

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."
    return aanbieding

print(aanbieding_1("aardbei", 4, 0.1))
def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde:.2f} euro."
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print(meervoudig([10,5,3,2,1,2,9]))

def mijn_functie_2(lijst):
    return sum(lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)

print(combinatie([10,5,3,2,1,2,9]))