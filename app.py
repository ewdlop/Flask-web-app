from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

@app.route('/signup', methods=['POST']) # decorator
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if not is_strong_password(password):
        return jsonify({"error": "Password is not strong enough"}), 400

    hashed_password = generate_password_hash(password)

    # Save the user to the database (this part is omitted for brevity)
    # ...

    return jsonify({"message": "User signed up successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
