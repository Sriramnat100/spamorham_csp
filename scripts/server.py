from flask import Flask, render_template, request, redirect, url_for
from analyze import analyzer

app = Flask(__name__)

formData = {}

@app.route("/home", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        given = request.form['fname']
        formData['given'] = given
        return redirect(url_for('output'))
    else:
        return render_template('index.html')



@app.route('/output')
def output():
    name=formData['given']
    work = analyzer(name)
    return render_template('output.html', work=work)

if __name__ == "__main__":
    app.run(debug=True)


#source /Users/sriramnatarajan/Documents/spamorham_csp/scripts/venv/bin/activate