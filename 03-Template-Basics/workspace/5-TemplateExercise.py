from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    # This home page should have the form.
    return render_template('3-index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    auth_user = {'lowercase': False, 'uppercase': False, 'number': False}
    username = request.args.get('username')

    auth_user['lowercase'] = any(c.islower() for c in username)
    auth_user['uppercase'] = any(c.isupper() for c in username)
    auth_user['number'] = username[-1].isdigit()

    return render_template('3-report.html', auth_user=auth_user, username=username)


if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
