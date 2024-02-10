from app import db, app  # Ensure 'app' is also imported

# push an application context
with app.app_context():
    # create the database and the database table
    db.create_all()

    # commit the changes
    db.session.commit()  # This line is unnecessary after db.create_all() and can be removed.