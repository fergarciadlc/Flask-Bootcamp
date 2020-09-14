from flask import Flask
app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    return "<h1>Puppy Latin name generator</h1>\n<p>Go to 'puppy_latin/&lt;name&gt;' to generate a puppy latin name!</p>"

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    lat_name = ''
    if name[-1].lower() == 'y':
        lat_name = name[:-1] + 'iful'
    else:
        lat_name = name + 'y'

    return f'<h1>{name} &rarr; {lat_name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
