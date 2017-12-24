# -*- coding: utf-8 -*-
"""A way to access exist db tables with sqlalchemy"""

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from models import db

Base = automap_base()

# reflect the tables
Base.prepare(db.engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
User = Base.classes.user
Address = Base.classes.address

session = Session(db.engine)

# rudimentary relationships are produced
session.add(Address(email_address="foo@bar.com", user=User(username="foo", email="foo")))
session.commit()
