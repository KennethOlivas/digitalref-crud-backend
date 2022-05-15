from config.settings import app
from flask_cors import CORS

CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()   