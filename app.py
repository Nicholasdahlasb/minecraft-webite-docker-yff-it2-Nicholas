from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('website.html')

@app.route('/server')
def server():
    return render_template('server.html')

if __name__ == '__main__':
    app.run(debug=True)