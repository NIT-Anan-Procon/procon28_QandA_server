from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name


@app.teardown_appcontext
def _close_db():
    print("close")

if __name__ == "__main__":
    app.run(debug=True)