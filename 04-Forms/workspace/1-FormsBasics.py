from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

# Sectret Key -> ANY STRING YOU WANT
app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''

    return render_template('1-index.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)
