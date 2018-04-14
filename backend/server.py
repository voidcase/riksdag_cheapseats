from flask import Flask
from routes.docs import documents

app = Flask(__name__)
app.register_blueprint(documents)

# returns json with all docs
if __name__ == '__main__':
    app.run(debug=True)
