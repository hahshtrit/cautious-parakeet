from __init__ import app, socket
import routes

if __name__ == "__main__":
    # enabling threading fixes 403 error on chrome, i think
    # nvm, it doesn't work, idk
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
    # socket.run(app, host="0.0.0.0", port=80, debug=True) # need to use this instead of above line for websockets to
    # work


# to run with docker, ensure that the url in browser is 127.0.0.1:8080, localhost:8080
# at least that worked for abi
