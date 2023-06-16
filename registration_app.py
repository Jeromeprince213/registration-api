#registration_app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from bcrypt import hashpw, gensalt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Initialize CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flaskmicroadmin:apolloatr@localhost/microservicesdb'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Generate salt and hash the password
    salt = gensalt()
    hashed_password = hashpw(password.encode('utf-8'), salt)

    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Registration successful!'})


if __name__ == '__main__':
    app.run(debug=True,port=5001)
