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

@app.route('/login_valid', methods=['POST'])
def login_valid():
    email = request.form.get('email')
    password = request.form.get('password')
    return "the email is {}".format(email)

if __name__ == '__main__':
    app.run(debug=True)