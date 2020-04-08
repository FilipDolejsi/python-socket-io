from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
import json

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'

socketio = SocketIO(app)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/startstop", methods=['POST'])
def start_stop_action():
    message = request.get_json()

    if "Action" in message:
        socketio.emit('action', message, broadcast=True)
        print(f"Message: {message['Action']} {' '.join([p['Name'] for p in message['Params']])}")

    if "Atomics" in message:
        socketio.emit('atomics', message["Atomics"], broadcast=True)
        print("Sent: " + json.dumps(message["Atomics"], indent=2))
    return "Ok"


@app.route('/api')
def api():
    query = dict(request.args)
    socketio.emit('log', dict(data=str(query)), broadcast=True)
    return jsonify(dict(success=True, message='Received'))


@socketio.on('connect')
def on_connect():
    payload = dict(data='Connected')
    emit('log', payload, broadcast=True)

@socketio.on('completed_action')
def on_action_completed(payload):
    print('Action completed: ' + str(payload))
    send(payload, broadcast=True)

@socketio.on('state_update')
def on_state_update(payload):
    print('State update: ' + str(payload))
    send(payload, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
