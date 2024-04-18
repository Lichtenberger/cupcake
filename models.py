from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = 'https://tinyurl.com/demo-cupcake'
db = SQLAlchemy()

class Cupcake(db.Model):
    ''' cupcake page '''

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text)

    def image_url(self):
        ''' cupcake photo '''

        return self.image or GENERIC_IMAGE
    def connect_db(app):
        ''' connect to flask app '''

        db.app = app
        db.init_app(app)