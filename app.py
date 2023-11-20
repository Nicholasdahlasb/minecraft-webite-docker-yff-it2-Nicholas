from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('website.html')

@app.route('/server')
def server():
    return render_template('server.html')

@app.route('/map')
def register():
    return render_template('map.html')

@app.route('/contact')
def contact():
    return redirect("https://discord.gg/uMwMdfDmQ2")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
