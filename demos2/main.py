from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import suppliste

app = Flask("Telefonbuch")

@app.route("/index")
def index():
    telbuchdaten = suppliste.telefonbuch_lesen()
    return render_template("suppliste.html", telbuch=telbuchdaten)

@app.route("/")
@app.route("/kal")
def kal():
    return render_template("kalo.html")


@app.route("/search/<name>")
@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    if (request.method == 'POST'):
        person_eintrag = suppliste.person_suchen(request.form)
        print(person_eintrag)
        return render_template("suppliste.html", telbuch=person_eintrag)

    return render_template("search.html")

@app.route("/add", methods=['GET', 'POST']) 
def add():
    if (request.method == 'POST'):
        suppliste.eintrag_speichern_von_formular(request.form)
        return redirect("/")

    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)