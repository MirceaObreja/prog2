from flask import Flask
from flask import render_template
from flask import request

app = Flask("Demo")



@app.route("/kalorienrechner/", methods=['GET', 'POST'])
def hallo():
	if request.method == 'POST':
		ziel_person = request.form['vorname']
		rueckgabe_string = "Hello " + ziel_person + "!"
		return rueckgabe_string

	return render_template("index.html", dinger= 2)




if __name__ == "__main__":
	app.run(debug=True, port=5000)
