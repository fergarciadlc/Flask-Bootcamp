from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    mylist = list(range(1,11))
    puppies = ['Fluffy', 'RRufus', 'Spike']
    return render_template('ControlFlow.html', mylist=mylist, puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)
