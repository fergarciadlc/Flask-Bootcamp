import os
from flask import Flask, render_template, url_for, redirect
from forms import AddPuppyForm, DelPuppyForm, AddOwnerForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# ==============================================================================
# SQL DB SECTION
# ==============================================================================
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# ==============================================================================
# Models (usually located in another file)
# ==============================================================================
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name: {self.name} and has no owner assigned yet"


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name: {self.name}"


# ==============================================================================
# Views - with Forms
# ==============================================================================
@app.route('/')
def index():
    return render_template('index.html')


# Add Puppy
@app.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddPuppyForm()

    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)

        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)


# list pup
@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()  # list of all puppies

    return render_template('list.html', puppies=puppies)


# Remove Puppy
@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelPuppyForm()

    if form.validate_on_submit():

        id = form.id.data

        puppy_id = Puppy.query.get(id)
        db.session.delete(puppy_id)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html', form=form)


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():

        name = form.name.data
        puppy_id = form.puppy_id.data

        # es necesaio esto? o puedo pasar solo puppy_id directo?
        # puppy = Puppy.query.get(puppy_id) # Respuesta: No es necesario, pasa solo puppy_id!

        # new_owner = Owner(name, puppy.id) #
        new_owner = Owner(name, puppy_id)

        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
