# CRUD
# CREATE READ UPDATE DELETE
from BasicModelApp import db, Puppy

# Create  a new entry in table:
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
all_puppies = Puppy.query.all()  # List of all puppy objects in the table
print(all_puppies)

# Select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filters by name
puppy_frankie = Puppy.query.filter_by(name='Frankie')  # Producing SQL commands
print(puppy_frankie.all())

# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

# PRINT ALL PUPPIES
all_puppies = Puppy.query.all()
print(all_puppies)
