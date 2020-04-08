from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'

socketio = SocketIO(app)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/startstop", methods=['POST'])
def start_stop_action():
    action = request.get_json()
    print(
        f"\Message: {action['Action']} {' '.join([p['Name'] for p in action['Params']])}")
    socketio.emit('action',action, broadcast = True)
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
def handleMessage(payload):
    print('You have: ' + str(payload))
    send(payload, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
