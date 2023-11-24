from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('website.html')

@app.route('/map')
def register():
    return render_template('map.html')

@app.route('/jesus')
def jesus():
    return render_template('jesus.html')

@app.route('/satan')
def satan():
    return render_template('satan.html')

@app.route('/contact')
def contact():
    return redirect("https://discord.gg/uMwMdfDmQ2")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
