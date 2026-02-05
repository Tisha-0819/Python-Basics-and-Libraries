# Task 4: Build a simple Flask app that serves a "Hello World" page with a form input.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <h1>Hello World!</h1>
    '''
if __name__ == '__main__':
    app.run(debug=True)

    
# To run the app, save this code in Task4.py and execute it.
# Then, open your web browser and go to http://