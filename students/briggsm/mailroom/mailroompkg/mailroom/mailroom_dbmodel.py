"""
    Simple database with Peewee ORM, sqlite and Python
    This script defines the schema
    Use logging for messages so they can be turned off

"""
import os
import mailroom as MR
from peewee import *

database = SqliteDatabase(os.path.dirname(MR.__file__) + '\\data\\mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database


#        Donor,
#        Donation



class Donor(BaseModel):
    """
        DB: this class defines a Donor, which is someone who has
        gives us cash.
    """
    donor_id = CharField(primary_key = True, max_length = 16)
    first_name = CharField(max_length = 30)
    lastname_name = CharField(max_length = 30)
    email = CharField(max_length = 40)

class Donation(BaseModel):
    """
        DB: This class defines a Donation.
    """
    donation_id = CharField(primary_key = True, max_length = 16)
    amount = DecimalField(max_digits = 7, decimal_places = 2)
    donor_id = ForeignKeyField(Donor, related_name='from_donor', null = False)