# seed.py

from app import app, db
from models import Cupcake
from flask import current_app

# Ensure the app is properly set up
with app.app_context():
    # Drop all tables
    db.drop_all()

    # Create the tables
    db.create_all()

    # Add sample cupcakes
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    # Add cupcakes to the session
    db.session.add_all([c1, c2])

    # Commit the changes
    db.session.commit()
