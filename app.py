from flask import render_template, Flask

app = Flask(name)

#main page
@app.route("/")
def home():
    render_template("index.html")

if name == 'main':
    app.run(host="0.0.0.0", port=8080)

# heyyyyyyyy
