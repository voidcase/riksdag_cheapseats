from flask import Flask
from routes import docs

app = Flask(__name__)
app.register_blueprint(docs)

# returns json with all docs
if __name__ == '__main__':
    app.run(debug=True)
