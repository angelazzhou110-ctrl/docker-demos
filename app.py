from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello from me!"

@app.get("/about")
def about():
    return "Read me!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 800)