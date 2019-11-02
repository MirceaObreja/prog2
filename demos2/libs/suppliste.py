import json

def telefonbuch_lesen():
    data = {}
    try:
        with open('telefonbuch.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data

def eintrag_speichern(name, telefon_nummer):
    telefonbuch = telefonbuch_lesen()
    telefonbuch[name] = {"name": name, "telefon": telefon_nummer}   
    print(telefonbuch)
    with open('telefonbuch.txt', "w", encoding="utf-8") as open_file:
        json.dump(telefonbuch, open_file)

def eintrag_speichern_von_formular(form_request):
    print(form_request)
    name = form_request.get('name')
    phone = form_request.get('phone')
    eintrag_speichern(name, phone)


def produkt_suchen(form_request):
    telefonbuch = telefonbuch_lesen()
    name = form_request.get('name')

    if name in telefonbuch:
        return {name: telefonbuch[name]}

def eintrag_speichern_von_kalo(form_request):
    print(form_request)
    name = form_request.get('name')
    phone = form_request.get('phone')
    eintrag_speichern(name, phone)

