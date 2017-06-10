from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from puppies import Base, Shelter, Puppy
from datetime import date

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# 1. Query all of the puppies and return the results in ascending alphabetical order
def allPuppiesAlphaOrder():
    return session.query(Puppy).order_by(Puppy.name).all()

# 2. Query all of the puppies that are less than 6 months old organized by the youngest first
def allPuppiesSixMonthsOld():
    return session.query(Puppy).order_by(Puppy.dateOfBirth).filter(Puppy.dateOfBirth > monthdelta(date.today(), -6))

# 3. Query all puppies by ascending weight
def allPuppiesWeight():
    return session.query(Puppy).order_by(Puppy.weight).all()

# 4. Query all puppies grouped by the shelter in which they are staying
def allPuppiesShelter():
    return session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
