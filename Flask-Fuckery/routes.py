from flask import Flask

app = Flask(__name__)
'''
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
'''

@app.route('/')
def hello_world():
    return 'Hello World!'
