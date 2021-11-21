from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/submit', method=["POST"])
def submit():
    if request.method == 'POST':
        name = request.form["username"]

    return render_template('submit.html', n=name)


if __name__ == '__main__':
    app.run(debug=True)
