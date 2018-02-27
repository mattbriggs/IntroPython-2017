from mailroom_dbmodel import *

with database.transaction():
    make_donor = Donor.create(
        donor_id = "123456789",
        first_name = "fname",
        lastname_name = "lname",
        email = "email@mail.com")
    make_donor.save()