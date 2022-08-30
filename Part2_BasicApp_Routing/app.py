from flask import Flask
from flask import render_template

# here we are going to modify to set the folders that contain our static files and templates
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

# exampe of how to take a argument from the url
@app.route('/hello/<name>') 
def hello_name(name):
    return 'Hello %s!' % name

# example of how to take a argument from the url and return a number
@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return '%d + %d = %d' % (x, y, x+y)

# example of how to set a new HTML file to be the default page
@app.route('/index')
def index():
    return render_template('index.html')



## Note, if you want to run this app with the command `python app.py`, you need to add the following line to the end of the file
## so it can execute and stay running....
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)