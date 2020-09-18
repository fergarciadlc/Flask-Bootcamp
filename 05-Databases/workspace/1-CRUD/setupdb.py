# This script cannot be run twice!
from BasicModelApp import db, Puppy

# Creates all the tables:
# transforms model classes to DB tables
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# None expected
print(sam.id)
print(frank.id)

# instead of: df.session.add(sam); df.session.add(frank)
db.session.add_all([sam, frank])

# save changes to database:
db.session.commit()

# ID expected
print(sam.id)
print(frank.id)
