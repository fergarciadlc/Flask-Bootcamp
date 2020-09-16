from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    name = "Sammy"
    letters = list(name)
    pup_dict = {'pup_name': 'Sammy'}
    return render_template('Basic-Template.html', name=name, letters=letters, pup_dict=pup_dict)


if __name__ == '__main__':
    app.run(debug=True)
