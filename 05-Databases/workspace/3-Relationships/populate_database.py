"""
Create entries into the tables
"""
from Models import db, Puppy, Toy, Owner

# Creating 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add puppies to database
db.session.add(rufus)
db.session.add(fido)
db.session.commit()

# Check!, print all puppies from the data base
print(Puppy.query.all())

# Grab Rufus
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create a owner for Rufus
jose = Owner('Jose', rufus.id)

# Give Rufus some toys
toy1 = Toy('Ball', rufus.id)
toy2 = Toy('Hueso', rufus.id)

# Add and commit changes to database
db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Grab Rufus after those additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()
