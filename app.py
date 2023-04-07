
from flask import Flask, abort, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os

from helpers import company
from generate_reply.generate_reply import generate

app = Flask(__name__)
CORS(app)

auth = HTTPBasicAuth()
users = {"admin": "pbkdf2:sha256:260000$FvVC880DFewSqTlE$65f87da5399a9bb72271f3837c6852d3ddc88066e4d135b2eb8fe6ad193e3c9e"}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
@app.errorhandler(502)
def resource_not_found(e):
    return jsonify(error=str(e)), 502

@app.route("/email", methods=['post'])
@auth.login_required
def generate_email():
    print() 
    req = request.get_json()
    prev = req["prev_email"]
    resp = req["resp_email"]
    
    email = generate(prev)
    resp["email"] = email
    if email is None:
        abort(502)
    
    return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
