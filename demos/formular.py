from flask import Flask
from flask import render_template
from flask import request

app = Flask("Demo")

@app.route("/hello/", methods=['GET', 'POST'])
def hallo():
	if request.method == 'POST':
		ziel_person = request.form['vorname']
		rueckgabe_string = "Hello " + ziel_person + "!"
		return rueckgabe_string

	return render_template("index.html")

if __name__ == "__formular__"
	app.run(debug=True, port=5000)