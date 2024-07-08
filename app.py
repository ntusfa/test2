from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello man'

@app.route('/age/<int:age>')
def userage(age):
    return 'i am ' + str(age) + ' years old'

@app.route('/user/<username>')
def username(username):
    return 'i am ' + username

if __name__ == '__main__':
    app.debug = True
    app.run()
    