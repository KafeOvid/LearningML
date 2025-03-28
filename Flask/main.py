from flask import Flask, render_template, request

app =Flask(__name__)
@app.route('/')
def login():
    return render_template('index.html')

@app.route('/register')
def about():
    return '<h1>About</h1>'

@app.route('/home')
def home():
    return '<h1>Home</h1>'


if __name__ == '__main__':
    app.run(debug=True)