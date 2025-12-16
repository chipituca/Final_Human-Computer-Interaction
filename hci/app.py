from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/content')
def content():
    return render_template('content.html')

@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)