"""Diverse Importe"""
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
import os
from libs import suppliste
from rechnungen import formeln

os.system("cls")

app = Flask("HealthCoach")

"""Supplement Seite Seite"""
@app.route("/")
@app.route("/index")
def index():
    prod_daten = suppliste.file_lesen('prod.txt')
    print(prod_daten)
    leb_daten = suppliste.file_lesen('leb.txt')
    print(leb_daten)
    return render_template("suppliste.html", prod=prod_daten, leb=leb_daten)

"""Person hinzufügen Seite"""
@app.route("/kal", methods=['GET', 'POST'])
def kal():
    if request.method == 'POST':
        ergebnis_dict = request.form

        weiblich = ergebnis_dict.get('weiblich')
        alter = ergebnis_dict.get('alter')
        groesse = ergebnis_dict.get('groesse')
        gewicht = ergebnis_dict.get('gewicht')
        aktivitaet = ergebnis_dict.get('aktivitaet')
        ziel = ergebnis_dict.get('ziel')
        training = ergebnis_dict.get('training')
        
        """unterscheidung männlich weiblich"""
        if weiblich == 'on':
            geschlecht = "w"
        else:
            geschlecht = "m"

        """differenzierung bei der Ziel Wahl"""
        if ziel == '0.85':
            start = 0
            end = 100
        elif ziel == '1':
            start = 100
            end = 200
        else:
            start = 200
            end = 99999

        kalorien = formeln.basic(geschlecht, alter, groesse, gewicht, aktivitaet, ziel, training)
        suppliste.eintrag_speichern_von_kalo(request.form, kalorien)
        return render_template("kalo.html", ergebnis=kalorien, suppliste=between_two_values(suppliste.file_lesen('prod.txt'), start, end), lebliste=between_two_values(suppliste.file_lesen('leb.txt'), start, end))

    return render_template("kalo.html", ergebnis=False)

"""Ausgabe der verschiedenen Einträge in den Dictionarys"""
def between_two_values(dictionary, start, end):
    matches = {}
    for key, value in dictionary.items():
        if start <= int(value) <= end:
             matches[key]=value
    return matches

"""Suchen Seite"""
@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    if (request.method == 'POST'):
        if request.form["submit"] == "supp":
            produkt_eintrag = suppliste.produkt_suchen(request.form)
            return render_template("suppliste.html", prod=produkt_eintrag)
        elif request.form["submit"] == "pers":
            personen_eintrag = suppliste.person_suchen(request.form)
            print(personen_eintrag)
            return render_template("personenliste.html", prod=personen_eintrag)
        elif request.form["submit"] == "leben":
            lebensmittel_eintrag = suppliste.lebensmittel_suchen(request.form)
            print(lebensmittel_eintrag)
            return render_template("suppliste.html", leb=lebensmittel_eintrag)
    return render_template("search.html")

"""Personen Seite"""
@app.route("/search_per", methods=['GET', 'POST'])
def search_per(name=None):
    per_daten = suppliste.file_lesen('kalo.txt')
    print(per_daten)
    return render_template("personenliste.html", prod=per_daten)

"""Produkt hinzufügen Seite"""
@app.route("/add", methods=['GET', 'POST']) 
def add():
    if (request.method == 'POST'):
        if request.form['action'] == 'add_supp':
            suppliste.eintrag_speichern_von_prod(request.form)
        elif request.form['action'] == 'add_leb':
            suppliste.eintrag_speichern_von_leb(request.form)
        return redirect("/add")

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)