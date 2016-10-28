from flask import Flask
app_lulu = Flask(__name__)

@app_lulu.route('/hello_world')
def hello_world():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    return 'Hello World!'

if __name__ == '__main__':
    app_lulu.run(debug=True)
