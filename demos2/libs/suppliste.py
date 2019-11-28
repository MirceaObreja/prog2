import json

def file_lesen(file_name):
    data = {}
    try:
        with open(file_name, "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
        data = {}

    return data

def eintrag_speichern(data, file_name):
    with open(file_name, "w", encoding="utf-8") as open_file:
        json.dump(data, open_file)

def eintrag_speichern_von_prod(form_request):
    name = form_request.get('name')
    cal = form_request.get('cal')

    prod = file_lesen('prod.txt')
    prod[name] = cal
    eintrag_speichern(prod, 'prod.txt')

def eintrag_speichern_von_leb(form_request):
    name_leb = form_request.get('name_leb')
    cal_leb = form_request.get('cal_leb')

    leb = file_lesen('leb.txt')
    leb[name_leb] = cal_leb
    eintrag_speichern(leb, 'leb.txt')

def eintrag_speichern_von_kalo(form_request, kalorien):
    name = form_request.get('name')
    weiblich = form_request.get('weiblich')
    alter = form_request.get('alter')
    groesse = form_request.get('groesse')
    gewicht = form_request.get('gewicht')
    aktivitaet = form_request.get('aktivitaet')
    ziel = form_request.get('ziel')
    training = form_request.get('training')


    if weiblich == 'on':
        geschlecht = "w"
    else:
        geschlecht = "m"

    kalo = file_lesen('kalo.txt')
    kalo[name] = {
        "name": name,
        "alter": alter,
        "geschlecht": geschlecht,
        "groesse": groesse,
        "gewicht": gewicht,
        "aktivitaet": aktivitaet,
        "ziel": ziel,
        "training": training,
        "kalorien": kalorien
    }

    eintrag_speichern(kalo, 'kalo.txt')




def produkt_suchen(form_request):
    prod_liste = file_lesen('prod.txt')
    name = form_request.get('name')

    if name in prod_liste:
        return {name: prod_liste[name]}

def person_suchen(form_request):
    pers_liste = file_lesen('kalo.txt')
    name = form_request.get('name')

    if name in pers_liste:
        return {name: pers_liste[name]}

def lebensmittel_suchen(form_request):
    leb_liste = file_lesen('leb.txt')
    name = form_request.get('name')

    if name in leb_liste:
        return {name: leb_liste[name]}