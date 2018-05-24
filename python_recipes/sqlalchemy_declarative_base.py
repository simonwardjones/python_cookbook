"""
Section:
    sqlalchemy

Author:
    Simon Ward-Jones

Description:
    An example defining a many to many relationship using an association
    class and then a many-to-one relationship and finally a one-to-one
    relationship

Tags:
    sqlalchemy, table, declarative_base, many-to-many
"""
from sqlalchemy import (Column, DateTime, String, Integer, ForeignKey,
                        func, Boolean, create_engine)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    children = relationship('Child',
                            secondary='association',
                            back_populates='parents')

    def __repr__(self):
        return f'Parent(name={self.name})'


class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    parents = relationship('Parent',
                           secondary='association',
                           back_populates='children')

    def __repr__(self):
        return f'Child(name={self.name})'


class Association(Base):
    __tablename__ = 'association'
    parent_id = Column(Integer, ForeignKey('parents.id'), primary_key=True)
    child_id = Column(Integer, ForeignKey('children.id'), primary_key=True)
    good_relationsip = Column(Boolean, server_default=true())
    parent = relationship("Parent", backref='parent_child_association')
    child = relationship("Child", backref='child_parent_association')

    def __repr__(self):
        return f'Association({self.parent})<==>{self.child})'


# Create the database (in memory)
engine = create_engine('sqlite://', echo=False)
# turn echo to True to print sql as it runs
Base.metadata.bind = engine
Base.metadata.create_all()

# sql
# CREATE TABLE parents (
#     id INTEGER NOT NULL,
#     name VARCHAR(255),
#     PRIMARY KEY (id),
#     UNIQUE (name)
# )
# CREATE TABLE children (
#     id INTEGER NOT NULL,
#     name VARCHAR(255),
#     PRIMARY KEY (id),
#     UNIQUE (name)
# )
# CREATE TABLE association (
#     parent_id INTEGER NOT NULL,
#     child_id INTEGER NOT NULL,
#     good_relationsip BOOLEAN DEFAULT 1,
#     PRIMARY KEY (parent_id, child_id),
#     FOREIGN KEY(parent_id) REFERENCES parents (id),
#     FOREIGN KEY(child_id) REFERENCES children (id),
#     CHECK (good_relationsip IN (0, 1))
# )

# Define obejcts
richard = Child(name='Richard')
paul = Child(name='Paul')
simon = Child(name='Simon')
ann = Parent(name='Ann')
stephen = Parent(name='Stephen')

# So lets add our work to the db
Session = sessionmaker(bind=engine)
session = Session()

for item in [ann, stephen, richard, paul, simon]:
    session.add(item)
session.commit()
# sample sql:
# INSERT INTO children (name) VALUES (?)
# ('Richard',)


# set the family up (the relations)
for child in [richard, paul, simon]:
    ann.children.append(child)
    stephen.children.append(child)

# extra detail:
# Having defined the back_poulates we can use these properties as expected
# before having commited to the db (via session.commit())
print(f'Ann has children: {ann.children}')

# However the association objects have not been created yet
session.commit()
# sql
# INSERT INTO association (parent_id, child_id) VALUES (?, ?)
# ((1, 2), (1, 3), (2, 1), (2, 2), (2, 3))

# Now that the associations have been created we can inspect one
# also demonstrating the querying
query = session.query(Association) \
               .join(Parent) \
               .join(Child) \
               .filter(Parent.name == 'Ann') \
               .filter(Child.name == 'Simon')
ann_simon = query.one()

print(f'ann_simon object has __repr__: {ann_simon} and they do'
      f'{"not" if not ann_simon.good_relationsip else "" } get on')
# ann_simon object has __repr__:
# Association(Parent(name=Ann))<==>Child(name=Simon)) and they do get on


# We can take this example further let's add Toys but only for the
# children. lets make it many toy for each child. let's assume they
# are selfish and a toy can only have one child

class Toy(Base):
    __tablename__ = 'toys'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('children.id'))
    name = Column(String(255), unique=True)
    child = relationship('Child', backref='toys')

    def __repr__(self):
        return f"Toy(name={self.name})"


# Make the new table
Toy.__table__.create()

football = Toy(name='Football')
playstation = Toy(name='playstation')
bat = Toy(name='bat')

richard.toys.append(football)
richard.toys.append(playstation)
bat.child = paul

session.commit()

print(f'bat belongs to {bat.child}')
# bat belongs to Child(name=Paul)
print(f'Richard has toys {richard.toys}')
# Richard has toys [Toy(name=Football), Toy(name=playstation)]

# Comin full circle let's define a one-to-one relationship
# let's add nicknames as a one-to-one


class Nickname(Base):
    __tablename__ = 'nicknames'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('children.id'))
    nickname = Column(String(255), unique=True)
    child = relationship('Child', backref=backref("nickname", uselist=False))

    def __repr__(self):
        return self.nickname

    def __str__(self):
        return self.nickname


# Make the new table
Nickname.__table__.create()

Si = Nickname(nickname='Si')
Rich = Nickname(nickname='Rich')
simon.nickname = Si
print(f'simon has nickname {simon.nickname} of type {type(simon.nickname)}')
# simon has nickname Si of type <class '__main__.Nickname'>
