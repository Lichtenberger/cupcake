from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'icanttellyou'

connect_db(app)

@app.route('/api/cupcakes')
def home_page():
    '''cupcake homepage'''

    return render_template('index.html')

@app.route('/api/cupcakes')
def get_cupcakes():
    '''data about all cupcakes'''

    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id')
def get_cupcake(id):
    '''data about single cupcake'''

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes', methods=['POST']) 
def create_cupcake():
    '''Create your cupcake'''

    data = request.json()

    cupcake = Cupcake(
        flavor=data['flavor'],
        fating=data['rating'],
        size=data['size'],
        image=data['image'] or NotImplemented
    )

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.to_dict()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    ''' update cupcakes '''

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    ''' delete a cupcake '''

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Deleted')