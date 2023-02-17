from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/destytojas/')
def destytojas():
    return render_template("destytojas.html")

@app.route('/studentas/')
def studentas():
    return render_template("studentas.html")

@app.route('/airida/')
def airida():
    return render_template("airida.html")

@app.route('/gisora/')
def gisora():
    return render_template('gisora.html')

if __name__ == "__main__":
    app.run(debug=True)
