from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_url_path='/static/')

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")
app.jinja_env.undefined = StrictUndefined

PORT = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=PORT)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/error")
def error():
    raise Exception("Error!")

if __name__ == "__main__":
    
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
