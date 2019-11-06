from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
import os

from libs import suppliste

os.system("cls")

app = Flask("Telefonbuch")

@app.route("/index")
def index():
    prod_daten = suppliste.file_lesen('prod.txt')
    print(prod_daten)
    return render_template("suppliste.html", prod=prod_daten)

@app.route("/" , methods=['GET', 'POST'])
@app.route("/kal", methods=['GET', 'POST'])
def kal():
    if (request.method == 'POST'):
        suppliste.eintrag_speichern_von_kalo(request.form)
        return redirect("/")

    return render_template("kalo.html")

@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    if (request.method == 'POST'):
        produkt_eintrag = suppliste.produkt_suchen(request.form)
        print(produkt_eintrag)
        return render_template("suppliste.html", prod=produkt_eintrag)

    return render_template("search.html")


@app.route("/search_per", methods=['GET', 'POST'])
def search_per(name=None):
    if (request.method == 'POST'):
        person_eintrag = suppliste.person_suchen(request.form)
        print(person_eintrag)
        return render_template("personenliste.html", prod=person_eintrag)

    return render_template("personenliste.html")


@app.route("/add", methods=['GET', 'POST']) 
def add():
    if (request.method == 'POST'):
        suppliste.eintrag_speichern_von_prod(request.form)
        return redirect("/")

    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)