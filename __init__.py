from flask import Flask
from flask_socketio import SocketIO
from secrets import token_urlsafe

app = Flask(__name__)
app.secret_key = token_urlsafe(16).encode()
socket = SocketIO(app, logger=True)


if __name__ == "__main__":
    # enabling threading fixes 403 error on chrome, i think
    # nvm, it doesn't work, idk
    app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)
    # socket.run(app, host="0.0.0.0", port=80, debug=True) # need to use this instead of above line for websockets to
    # work


