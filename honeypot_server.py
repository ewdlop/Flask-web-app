from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the honeypot server!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    log_attack(username, password)
    return "Login failed!"

def log_attack(username, password):
    # 將攻擊者的行為記錄下來
    with open("attack_log.txt", "a") as file:
        file.write(f"Attempted login with Username: {username}, Password: {password}\n")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
