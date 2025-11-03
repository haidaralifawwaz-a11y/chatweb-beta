from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MVOqI1pGs3zF9WJsAYQcp9NXljEbB8Z14j16QpChAvA'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('login')
def handle_login(username):
    send({'username': 'SERVER', 'msg': f'{username} has joined the chat!'}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    print(f"{data['username']}: {data['msg']}")
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
