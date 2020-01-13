"""zuerst die einzelnen Formeln beschrieben und dann ganz unten in einer Formel zusammengeführt """

def kalorien_berechnen(alter):
    neuer_preis = alter - (alter * 0.1)
    return neuer_preis



"""Formel aufgeteilt für den Grundumsatz"""
def grundumsatz(request):
    if geschlecht == "m":
    	grundumsatz = (10 * int(gewicht)) + (6.25 * int(groesse)) - (5 * int(alter)) + 5 
    	kalorien_bedarf = grundumsatz * faktor_m
    else:
    	grundumsatz = (10 * int(gewicht)) + (6.25 * int(groesse)) - (5 * int(alter)) - 161
    	kalorien_bedarf = grundumsatz * faktor_w
    	return kalorien_bedarf



"""Formel für den Kalorienbedarf"""
def kalorienbedarf():
	if geschlecht == m:
		kalorien_bedarf = grundumsatz * faktor_m
	else:
		kalorien_bedarf = grundumsatz * faktor_m
	return kalorien_bedarf


"""Formel für den Kaloriennedarf zusammen gefügt"""
def basic(geschlecht, alter, groesse, gewicht, aktivitaet, ziel, training):
	alter = int(alter)
	groesse = int(groesse)
	gewicht = int(gewicht)
	aktivitaet = float(aktivitaet)
	ziel = float(ziel)
	training = int(training)

	if geschlecht == "w":
		kalorien_bedarf = ((10 * gewicht) + (6.25 * groesse) - (5 * alter) - 161) * aktivitaet
	else:
		kalorien_bedarf = ((10 * gewicht) + (6.25 * groesse) - (5 * alter) + 5) * aktivitaet 
	
	return kalorien_bedarf