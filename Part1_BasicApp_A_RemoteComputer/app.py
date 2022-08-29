from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, WWW!'


## Note, if you want to run this app with the command `python app.py`, you need to add the following line to the end of the file
## so it can execute and stay running....
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

##Notes: 
# - The `debug=True` is used to enable debug mode. This means you have HOT-RELOADING enabled.
    # the hot reload though does not work with the port number changes, you need to restart the server.
# - The `host=' is used to set the host to listen on, use 0.0.0.0 or localhost to listen on all interfaces.
    # this mean you can open up your browser an go to either `localhost` as the website, or `127.0.0.1` as the website.
# - The `port=80` is used to set the port to listen on. you can change this to whatever open port you want.
    # if you change the port, you need to update your website address to 0.0.0.0:8080 or localhost:8080 as an example 