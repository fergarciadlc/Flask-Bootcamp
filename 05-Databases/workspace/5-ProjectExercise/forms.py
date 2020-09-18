from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddPuppyForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy!')


class DelPuppyForm(FlaskForm):

    id = IntegerField('Id of Puppy to remove: ')
    submit = SubmitField('Remove Puppy')


class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner:')
    puppy_id = IntegerField('ID of Puppy:')
    submit = SubmitField('Add Owner')
