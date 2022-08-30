from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)

## Note, if you want to run this app with the command `python app.py`, you need to add the following line to the end of the file
## so it can execute and stay running....

## app @ decorator is a function that takes a function as an argument and returns a function
## from source code: https://github.com/pallets/flask/blob/c74f46979a8b8358437bd7f76e478d04248a9c72/flask/app.py#L1156 
## nice explanation here: https://stackoverflow.com/questions/46123448/how-do-decorated-functions-work-in-flask-python-app-route 
## In your code, @app.route("/") is a decorator which adds an endpoint to the app object. 
## It doesn't actually modify any behavior of the function, and is instead sugar to simplify the process.
## Without the route() decorator, this is how you'd do the equivalent route registration in Flask.

## What is __name__ = __main__ ?
## The condition if __name__ == ‘__main__’ is used in a Python program to execute the code inside 
## the if statement only when the program is executed directly by the Python interpreter. When the code 
## in the file is imported as a module the code inside the if statement is not executed.

##Notes: 
# - The `debug=True` is used to enable debug mode. This means you have HOT-RELOADING enabled.
    # the hot reload though does not work with the port number changes, you need to restart the server.
# - The `host=' is used to set the host to listen on, use 0.0.0.0 or localhost to listen on all interfaces.
    # this mean you can open up your browser an go to either `localhost` as the website, or `127.0.0.1` as the website.
# - The `port=80` is used to set the port to listen on. you can change this to whatever open port you want.
    # if you change the port, you need to update your website address to 0.0.0.0:8080 or localhost:8080 as an example 