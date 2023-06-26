@app.route('/',  defaults={'equipo': ''})
@app.route("/equipo/<equipo>")
def index(equipo=''):
    return render_template('layout.html', equipo=equipo)