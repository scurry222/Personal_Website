from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_url_path='/static/')

PORT = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=PORT)

@app.route("/")
def home():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)