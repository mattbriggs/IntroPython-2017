"""
    Create database with Peewee ORM, sqlite and Python.

    Note: Only run this if the DB does not exist.

"""

from mailroom_dbmodel import *

database.create_tables([
        Donor,
        Donation
    ])

database.close()
