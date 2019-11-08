def kalorien_berechnen(alter):
    neuer_preis = alter - (alter * 0.1)
    return neuer_preis


def grundumsatz():
	if geschlecht == m:
		grundumsatz = (10 * int(gewicht)) + (6.25 * int(groesse)) - (5 * int(alter)) + 5 
		kalorien_bedarf = grundumsatz * faktor_m
	else:
		grundumsatz = (10 * int(gewicht)) + (6.25 * int(groesse)) - (5 * int(alter)) - 161
		kalorien_bedarf = grundumsatz * faktor_w
	return kalorien_bedarf


def kalorienbedarf():
	if geschlecht == m:
		kalorien_bedarf = grundumsatz * faktor_m
	else:
		kalorien_bedarf = grundumsatz * faktor_m
	return kalorien_bedarf

def basic():
	if geschlecht_weiblich == "weiblich":
		kalorien_bedarf = alter * 3
	else:
		kalorien_bedarf = alter * 5
	return kalorien_bedarf