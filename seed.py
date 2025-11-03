from app import create_app, db
from app.models.cat import Cat

my_app = create_app()
with my_app.app_context():
    db.create_all()
    db.session.add(Cat(name = "Jason", color = "black", personality = "love love love love"))
    db.session.add(Cat(name = "Jason", color = "black", personality = "love love love love"))
    db.session.add(Cat(name = "Jojo", color = "orange", personality = "love love koko love love"))

    db.session.commit()
